from lib2to3.pgen2.token import COLON
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import *
'''
from main.d96.utils.AST import *
from main.d96.parser.D96Parser import D96Parser
from main.d96.parser.D96Visitor import D96Visitor
# '''
class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(list(map(lambda x: self.visit(x), ctx.class_declaration())))
    
    
    def visitClass_declaration(self, ctx: D96Parser.Class_declarationContext):
        class_name = Id(str(ctx.NORMAL_ID(0).getText()))
        
        list_of_mem = self.check_main_method(self.visit(ctx.list_of_members()) if ctx.list_of_members() else [], class_name.name)
        
        parent_name = Id(str(ctx.NORMAL_ID(1).getText())) if ctx.COLLON() else None

        return ClassDecl(class_name, list_of_mem, parent_name)


    def check_main_method(self, list_of_members, class_name):
        for member in list_of_members:
            if isinstance(member,MethodDecl) and member.name.name == 'main' and class_name == 'Program' and len(member.param) == 0:
                member.kind = Static()
        
        return list_of_members


    def visitList_of_members(self, ctx: D96Parser.List_of_membersContext):
        return reduce(lambda a, b: a + (self.visit(b) if isinstance(self.visit(b),list) else [self.visit(b)]), ctx.member(), [])


    def visitMember(self, ctx: D96Parser.MemberContext):
        return self.visit(ctx.getChild(0)) if ctx.getChildCount() == 1 else []


    def visitAttribute_declaration(self, ctx: D96Parser.Attribute_declarationContext):
        decl = VarDecl if ctx.VAR() else ConstDecl
        name_list, type_name, expr_list = self.visit(ctx.getChild(1))
        if ctx.attr_decl_bis():
            return list(map(lambda name, expr: AttributeDecl(Static() if name[0] == '$' else Instance(), decl(Id(name),type_name, expr)), name_list, expr_list))
                
        return list(map(lambda name: AttributeDecl(Static() if name[0] == '$' else Instance(),decl(Id(name),type_name,NullLiteral() if isinstance(type_name,ClassType) else None)), name_list))

    
    def visitAttr_decl_bis(self, ctx: D96Parser.Attr_decl_bisContext):
        if ctx.COLLON():
            name, type_name, expr = [], self.visit(ctx.type_name()),[]  
        else: name, type_name, expr = self.visit(ctx.attr_decl_bis())
        
        return [self.visit(ctx.possible_id())] + name, type_name, expr+ [self.visit(ctx.expression())]


    def visitAttr_decl_bis1(self, ctx: D96Parser.Attr_decl_bis1Context):
        return self.visit(ctx.id_list_attribute()), self.visit(ctx.type_name()), []


    def visitPossible_id(self, ctx: D96Parser.Possible_idContext):
        return ctx.getChild(0).getText()


    def visitId_list_attribute(self, ctx: D96Parser.Id_list_attributeContext):
        return [self.visit(ctx.getChild(0))] + (self.visit(ctx.getChild(1)) if ctx.more_id_attribute() else [])
        

    def visitMore_id_attribute(self, ctx: D96Parser.More_id_attributeContext):
        return self.visit(ctx.id_list_attribute())


    def visitType_name(self, ctx: D96Parser.Type_nameContext):
        if ctx.array_type():
            type_name = self.visit(ctx.array_type())
        elif ctx.INT():
            type_name = IntType()
        elif ctx.FLOAT():
            type_name = FloatType()
        elif ctx.BOOLEAN():
            type_name = BoolType()
        elif ctx.STRING():
            type_name = StringType()
        else: type_name = ClassType(Id(ctx.NORMAL_ID().getText()))

        return type_name


    def visitMethod_declaration(self, ctx: D96Parser.Method_declarationContext):
        return self.visit(ctx.getChild(0))


    def visitNormal_method(self, ctx: D96Parser.Normal_methodContext):
        name = self.visit(ctx.possible_id())
        kind = Static() if name[0] == '$' else Instance()
        body = self.visit(ctx.block_stmt()) 
        var_decl = self.visit(ctx.list_of_parameters()) if ctx.list_of_parameters() else []
        
        return MethodDecl(kind,Id(name),var_decl,body)


    def visitConstructor(self, ctx: D96Parser.ConstructorContext):
        name = str(ctx.CONSTRUCTOR().getText())
        kind = Instance()
        body = self.visit(ctx.block_stmt())
        var_decl = self.visit(ctx.list_of_parameters()) if ctx.list_of_parameters() else []
        
        return MethodDecl(kind,Id(name),var_decl,body)


    def visitDestructor(self, ctx: D96Parser.DestructorContext):
        name = str(ctx.DESTRUCTOR().getText())
        kind = Instance()
        body = self.visit(ctx.block_stmt())
        var_decl = []
        
        return MethodDecl(kind,Id(name),var_decl,body)

    
    def visitList_of_parameters(self, ctx: D96Parser.List_of_parametersContext):
        return reduce(lambda a,b: a + self.visit(b), ctx.parameters(),[]) 


    def visitParameters(self, ctx: D96Parser.ParametersContext):
        return list(map(lambda name: VarDecl(Id(name), self.visit(ctx.type_name())), self.visit(ctx.id_list())))  


    def visitId_list(self, ctx: D96Parser.Id_listContext):
        return reduce(lambda a,b: a + [b.getText()], ctx.NORMAL_ID(),[])

    
    def visitList_of_expressions(self, ctx: D96Parser.List_of_expressionsContext):
        return [self.visit(x) for x in ctx.expression()]      


    def visitExpression(self, ctx: D96Parser.ExpressionContext):
        return self.visit(ctx.getChild(0))


    def visitString_expression(self, ctx: D96Parser.String_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))


    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        return self.visit(ctx.relation_expression())


    def visitRelation_expression(self, ctx: D96Parser.Relation_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))


    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        return self.visit(ctx.getChild(0))


    def visitLogical_expression(self, ctx: D96Parser.Logical_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        return self.visit(ctx.getChild(0))


    def visitAdding_expression(self, ctx: D96Parser.Adding_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))


    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        return self.visit(ctx.getChild(0))
    

    def visitMultiplying_expression(self, ctx: D96Parser.Multiplying_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))


    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        return self.visit(ctx.not_expression())


    def visitNot_expression(self, ctx: D96Parser.Not_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        
        return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.getChild(1)))


    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        return self.visit(ctx.negative_expression())


    def visitNegative_expression(self, ctx: D96Parser.Negative_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        
        return UnaryOp(ctx.SUB().getText(),self.visit(ctx.expr6()))


    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        list_exprs = self.visit(ctx.index_expression())
        if len(list_exprs) == 1:
            return list_exprs[0]
        
        return self.rearrange_index_expr(list_exprs)
        

    def rearrange_index_expr(self, list_exprs):
        return ArrayCell(list_exprs[0],list_exprs[1:])


    def visitIndex_expression(self, ctx: D96Parser.Index_expressionContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr8())]
        
        return self.visit(ctx.index_expression()) + [self.visit(ctx.expression())]


    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        return self.visit(ctx.object_access_expression())


    def visitObject_access_expression(self, ctx: D96Parser.Object_access_expressionContext):
        if ctx.NORMAL_ID():
            if ctx.LB():
                return CallExpr(self.visit(ctx.object_access_expression()),Id(ctx.NORMAL_ID().getText()),self.visit(ctx.list_of_expressions()) if ctx.list_of_expressions() else [])
            
            return FieldAccess(self.visit(ctx.object_access_expression()),Id(ctx.NORMAL_ID().getText()))
        
        if ctx.static_ob_access():
            return self.visit(ctx.static_ob_access())
        
        if ctx.static_mth_access():
            return self.visit(ctx.static_mth_access())
        
        return self.visit(ctx.expr9())


    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        return self.visit(ctx.operand()) if ctx.operand() else self.visit(ctx.object_creation_expression())


    def visitOperand(self, ctx: D96Parser.OperandContext):
        if ctx.all_literals():
            return self.visit(ctx.all_literals())
        if ctx.NORMAL_ID():
            return Id(ctx.NORMAL_ID().getText())
        if ctx.SELF():
            return SelfLiteral()
        
        return self.visit(ctx.expression())


    def visitAll_literals(self, ctx: D96Parser.All_literalsContext):
        if ctx.all_int_lit():
            return self.visit(ctx.all_int_lit())
        if ctx.FLOAT_LIT():
            return FloatLiteral(float((lambda x: x if x[0] != '.' else '0' + x)(ctx.FLOAT_LIT().getText())))
        if ctx.STR_LIT():
            return StringLiteral(ctx.STR_LIT().getText())
        if ctx.BOOL_LIT():
            return BooleanLiteral(ctx.BOOL_LIT().getText() == 'True')
        if ctx.array_lit():
            return self.visit(ctx.array_lit())

        return NullLiteral()
        
        
    def visitInst_ob_access(self, ctx: D96Parser.Inst_ob_accessContext):
        return FieldAccess(self.visit(ctx.object_access_expression()),Id(ctx.NORMAL_ID().getText()))

    def visitInst_mth_access(self, ctx: D96Parser.Inst_mth_accessContext):
        return CallStmt(self.visit(ctx.super_inst_mth_acess()),Id(ctx.NORMAL_ID().getText()),self.visit(ctx.list_of_expressions()) if ctx.list_of_expressions() else [])

    def visitSuper_inst_mth_acess(self, ctx: D96Parser.Super_inst_mth_acessContext):
        if ctx.NORMAL_ID():
            if ctx.LB():
                return CallExpr(self.visit(ctx.super_inst_mth_acess()),Id(ctx.NORMAL_ID().getText()),self.visit(ctx.list_of_expressions()) if ctx.list_of_expressions() else [])
            
            return FieldAccess(self.visit(ctx.super_inst_mth_acess()),Id(ctx.NORMAL_ID().getText()))
        
        if ctx.static_ob_access():
            return self.visit(ctx.static_ob_access())
        
        if ctx.static_mth_access():
            return self.visit(ctx.static_mth_access())
        
        return self.visit(ctx.expr9())


    def visitStatic_ob_access(self, ctx: D96Parser.Static_ob_accessContext):
        return FieldAccess(Id(ctx.NORMAL_ID().getText()), Id(ctx.DOLLAR_ID().getText()))

    def visitStatic_mth_access(self, ctx: D96Parser.Static_mth_accessContext):
        return CallExpr(Id(ctx.NORMAL_ID().getText()), Id(ctx.DOLLAR_ID().getText()), self.visit(ctx.list_of_expressions()) if ctx.list_of_expressions() else [])

    def visitObject_creation_expression(self, ctx: D96Parser.Object_creation_expressionContext):
        return NewExpr(Id(ctx.NORMAL_ID().getText()), self.visit(ctx.list_of_expressions()) if ctx.list_of_expressions() else [])

    def visitStatements(self, ctx: D96Parser.StatementsContext):
        if ctx.var_and_const_stmt():
            return self.visit(ctx.var_and_const_stmt())
        if ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.for_in_stmt():
            return self.visit(ctx.for_in_stmt())
        if ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        if ctx.cont_stmt():
            return self.visit(ctx.cont_stmt())
        if ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        if ctx.method_invocation_stmt():
            return self.visit(ctx.method_invocation_stmt())
        
        return self.visit(ctx.block_stmt())

    def visitVar_and_const_stmt(self, ctx: D96Parser.Var_and_const_stmtContext):
        decl = VarDecl if ctx.VAR() else ConstDecl   
        name_list, type_name, expr_list = self.visit(ctx.getChild(1))     
        if expr_list != []:            
            return list(map(lambda name, expr: decl(Id(name),type_name, expr), name_list, expr_list))
                
        return list(map(lambda name: decl(Id(name),type_name,NullLiteral() if isinstance(type_name,ClassType) else None), name_list))


    def visitVar_and_const_bis(self, ctx: D96Parser.Var_and_const_bisContext):
        if ctx.var_and_const_bis():
            name, type_name, expr = self.visit(ctx.var_and_const_bis()) 
        else: name, type_name, expr = [], self.visit(ctx.type_name()), []

        return [ctx.NORMAL_ID().getText()] + name, type_name, expr + [self.visit(ctx.expression())]


    def visitVar_and_const_bis1(self, ctx: D96Parser.Var_and_const_bis1Context):
        name_list = list(map(lambda x: x.getText(), ctx.NORMAL_ID()))
        type_name = self.visit(ctx.type_name())

        return name_list, type_name, []


    def visitAssign_stmt(self, ctx: D96Parser.Assign_stmtContext):
        return Assign(self.visit(ctx.left_hand_side()), self.visit(ctx.expression()))

    def visitLeft_hand_side(self, ctx: D96Parser.Left_hand_sideContext):
        return self.rearrange_index_expr(self.visit(ctx.getChild(0)) + [self.visit(ctx.expression())]) if ctx.index_expression() else self.visitChildren(ctx)
        

    def visitScalar_var(self, ctx: D96Parser.Scalar_varContext):
        return Id(ctx.NORMAL_ID().getText()) if ctx.NORMAL_ID() else self.visit(ctx.getChild(0))


    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        if ctx.ELSEIF():
            right = self.visit(ctx.block_stmt()[-1]) if ctx.ELSE() else None
            exprs = list(reversed(list(map(lambda x: self.visit(x), ctx.expression()))))
            blocks = list(reversed(list(map(lambda x: self.visit(x), ctx.block_stmt()))))
            if ctx.ELSE(): blocks = blocks[1:]

            for expr, block in zip(exprs, blocks):
                right = If(expr, block, right)
            
            return right
        
        return If(self.visit(ctx.expression(0)), self.visit(ctx.block_stmt(0)), self.visit(ctx.block_stmt(1)) if ctx.ELSE() else [])


    def visitFor_in_stmt(self, ctx: D96Parser.For_in_stmtContext):
        name = ctx.NORMAL_ID().getText()
        exprs = list(map(lambda x: self.visit(x), ctx.expression()))
        loop = self.visit(ctx.block_stmt())
                
        return For(Id(name),exprs[0],exprs[1],loop,exprs[2] if len(exprs) == 3 else IntLiteral(1))


    def visitBreak_stmt(self, ctx: D96Parser.Break_stmtContext):
        return Break()

    def visitCont_stmt(self, ctx: D96Parser.Cont_stmtContext):
        return Continue()
    
    def visitReturn_stmt(self, ctx: D96Parser.Return_stmtContext):
        return Return(self.visit(ctx.expression()) if ctx.expression()else None)


    def visitMethod_invocation_stmt(self, ctx: D96Parser.Method_invocation_stmtContext):
        method_access = self.visit(ctx.getChild(0))
        
        return method_access if isinstance(method_access,CallStmt) else CallStmt(method_access.obj, method_access.method, method_access.param)


    def visitBlock_stmt(self, ctx: D96Parser.Block_stmtContext):
        return Block(reduce(lambda a, b: a + (self.visit(b) if isinstance(self.visit(b),list) else [self.visit(b)]), ctx.statements(), []))


    def visitArray_lit(self, ctx: D96Parser.Array_litContext):        
        return self.visit(ctx.getChild(0))


    def visitIndexed_array(self, ctx: D96Parser.Indexed_arrayContext):
        return ArrayLiteral(self.visit(ctx.list_of_expressions())) if ctx.list_of_expressions() else ArrayLiteral([])


    def visitMulti_demensional_array(self, ctx: D96Parser.Multi_demensional_arrayContext):
        return ArrayLiteral(self.visit(ctx.list_of_arrays()))


    def visitList_of_arrays(self, ctx: D96Parser.List_of_arraysContext):
        return [self.visit(ctx.indexed_array())] + (self.visit(ctx.more_array()) if ctx.more_array() else [])


    def visitMore_array(self, ctx: D96Parser.More_arrayContext):
        return self.visit(ctx.list_of_arrays())


    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        try: 
            num = int(ctx.INT_LIT().getText(),0)
        except:
            num = int(ctx.INT_LIT().getText(),8)
        
        return ArrayType(num, self.visit(ctx.type_name()))


    def visitAll_int_lit(self, ctx: D96Parser.All_int_litContext):
        try:
            return IntLiteral(int(ctx.getChild(0).getText(),0))
        except:
            return IntLiteral(int(ctx.getChild(0).getText(),8))
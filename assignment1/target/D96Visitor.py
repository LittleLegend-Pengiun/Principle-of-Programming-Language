# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declaration.
    def visitClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_members.
    def visitList_of_members(self, ctx:D96Parser.List_of_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_declaration.
    def visitAttribute_declaration(self, ctx:D96Parser.Attribute_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_decl_bis.
    def visitAttr_decl_bis(self, ctx:D96Parser.Attr_decl_bisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_decl_bis1.
    def visitAttr_decl_bis1(self, ctx:D96Parser.Attr_decl_bis1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#possible_id.
    def visitPossible_id(self, ctx:D96Parser.Possible_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_list_attribute.
    def visitId_list_attribute(self, ctx:D96Parser.Id_list_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#more_id_attribute.
    def visitMore_id_attribute(self, ctx:D96Parser.More_id_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#value_list.
    def visitValue_list(self, ctx:D96Parser.Value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#type_name.
    def visitType_name(self, ctx:D96Parser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_declaration.
    def visitMethod_declaration(self, ctx:D96Parser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#normal_method.
    def visitNormal_method(self, ctx:D96Parser.Normal_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_parameters.
    def visitList_of_parameters(self, ctx:D96Parser.List_of_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#more_parameters.
    def visitMore_parameters(self, ctx:D96Parser.More_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameters.
    def visitParameters(self, ctx:D96Parser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_list.
    def visitId_list(self, ctx:D96Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#more_id.
    def visitMore_id(self, ctx:D96Parser.More_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_expressions.
    def visitList_of_expressions(self, ctx:D96Parser.List_of_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#more_expression.
    def visitMore_expression(self, ctx:D96Parser.More_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_expression.
    def visitString_expression(self, ctx:D96Parser.String_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relation_expression.
    def visitRelation_expression(self, ctx:D96Parser.Relation_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#logical_expression.
    def visitLogical_expression(self, ctx:D96Parser.Logical_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#adding_expression.
    def visitAdding_expression(self, ctx:D96Parser.Adding_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multiplying_expression.
    def visitMultiplying_expression(self, ctx:D96Parser.Multiplying_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#not_expression.
    def visitNot_expression(self, ctx:D96Parser.Not_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#negative_expression.
    def visitNegative_expression(self, ctx:D96Parser.Negative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_expression.
    def visitIndex_expression(self, ctx:D96Parser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_access_expression.
    def visitObject_access_expression(self, ctx:D96Parser.Object_access_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operand.
    def visitOperand(self, ctx:D96Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#all_literals.
    def visitAll_literals(self, ctx:D96Parser.All_literalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#inst_ob_access.
    def visitInst_ob_access(self, ctx:D96Parser.Inst_ob_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#inst_mth_access.
    def visitInst_mth_access(self, ctx:D96Parser.Inst_mth_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#super_inst_mth_acess.
    def visitSuper_inst_mth_acess(self, ctx:D96Parser.Super_inst_mth_acessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_ob_access.
    def visitStatic_ob_access(self, ctx:D96Parser.Static_ob_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_mth_access.
    def visitStatic_mth_access(self, ctx:D96Parser.Static_mth_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_creation_expression.
    def visitObject_creation_expression(self, ctx:D96Parser.Object_creation_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statements.
    def visitStatements(self, ctx:D96Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_and_const_stmt.
    def visitVar_and_const_stmt(self, ctx:D96Parser.Var_and_const_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_and_const_bis.
    def visitVar_and_const_bis(self, ctx:D96Parser.Var_and_const_bisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_and_const_bis1.
    def visitVar_and_const_bis1(self, ctx:D96Parser.Var_and_const_bis1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#left_hand_side.
    def visitLeft_hand_side(self, ctx:D96Parser.Left_hand_sideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_var.
    def visitScalar_var(self, ctx:D96Parser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_stmt.
    def visitFor_in_stmt(self, ctx:D96Parser.For_in_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#cont_stmt.
    def visitCont_stmt(self, ctx:D96Parser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invocation_stmt.
    def visitMethod_invocation_stmt(self, ctx:D96Parser.Method_invocation_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_lit.
    def visitArray_lit(self, ctx:D96Parser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexed_array.
    def visitIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_demensional_array.
    def visitMulti_demensional_array(self, ctx:D96Parser.Multi_demensional_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_arrays.
    def visitList_of_arrays(self, ctx:D96Parser.List_of_arraysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#more_array.
    def visitMore_array(self, ctx:D96Parser.More_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#all_int_lit.
    def visitAll_int_lit(self, ctx:D96Parser.All_int_litContext):
        return self.visitChildren(ctx)



del D96Parser
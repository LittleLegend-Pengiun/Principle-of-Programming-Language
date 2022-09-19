from AST import * 
from Visitor import *
from StaticError import *
from functools import reduce

from main.d96.utils.AST import * 

NO_SUPER_CLASS = "No super class"
CURRENT_METHOD = "current method"
CLASS_ATTRIBUTES = "class attributes"

class type_for_checking:
    def __init__(self, obj_kind: str, is_instance: bool, obj_type, method_param_type = None):
        self.obj_kind = obj_kind
        self.is_instance = is_instance
        self.obj_type = obj_type
        self.method_param_type = method_param_type

class Tools:
    @staticmethod
    def compare_type_from_obj(type1, type2):
        if (type(type1) == type(type2)):
            if type(type1) == ArrayType:
                if type1.size != type2.size or not Tools.compare_type_from_obj(type1.eleType, type2.eleType):
                    return False
            if type(type1) == ClassType:
                if type1.classname.name != type2.classname.name:
                    return False
            return True
        return False
    
    @staticmethod
    def if_type_is_compatible(lhs, rhs, super_cls_list=None):        
        if (type(lhs) == ArrayType and type(rhs) == ArrayType) and lhs.size == rhs.size and (Tools.compare_type_from_obj(lhs.eleType, rhs.eleType) or Tools.if_type_is_compatible(lhs.eleType, rhs.eleType, super_cls_list)):
            return True
        
        if type(lhs) == FloatType and type(rhs) == IntType: 
            return True
        if type(lhs) == ClassType and type(rhs) == NullLiteral:
            return True
        
        return False
    
    @staticmethod
    def get_id_type_in_cur_scope(name, scope):
        if isinstance(scope, list):
            for small_dict in scope:
                if name in small_dict: return small_dict[name]
        if isinstance(scope, dict) and name in scope: 
            return scope[name]
        
        return None
    
    @staticmethod
    def compare_paras_type_btwn_method_and_call(method_para, call_para, super_cls_list=None):
        if len(method_para) == len(call_para) == 0:
            return True

        if len(method_para) != len(call_para): 
            return False
        
        tmp_func = lambda lhs, rhs: Tools.compare_type_from_obj(lhs, rhs) or Tools.if_type_is_compatible(lhs, rhs, super_cls_list)
        
        return reduce(lambda x,y: x == y == True, list(map(tmp_func, method_para, call_para)))
    
    @staticmethod
    def get_field_type_of_class(name, class_name, scope, is_method=False):
        if not is_method and name in scope[class_name][CLASS_ATTRIBUTES]:
            return scope[class_name][CLASS_ATTRIBUTES][name]
        if name in scope[class_name]:
            return scope[class_name][name]
        return None

    @staticmethod
    def check_class_inheritance(class_name, super_class_name, inheritance_map):
        if class_name == super_class_name:
            return True
        
        if class_name == NO_SUPER_CLASS:
            return False

        return Tools.check_class_inheritance(inheritance_map[ class_name], super_class_name, inheritance_map)


class StaticChecker(BaseVisitor):        
    def __init__(self,ast):
        self.ast = ast
        self.cur_mth = None
        self.cur_cls = None
        self.is_program_main_cls = False
        self.global_scope = {}
        self.inheritance_map = {}
        self.is_in_loop = {}
        self.array_lit = None
        self.if_statement = None

    def check(self):
        return self.visit(self.ast, None)


    def visitProgram(self, ast: Program, _):
        no_program_class = True
        for x in ast.decl:
            temp = self.visit(x, {})
            if x.classname.name == "Program":
                no_program_class = False
            if temp: raise NoEntryPoint()
        
        if no_program_class: 
            raise NoEntryPoint()
        
        return []


    def visitClassDecl(self, ast: ClassDecl, _):
        if ast.classname.name in self.global_scope:
            raise Redeclared(Class(), ast.classname.name)
        # Method and static attributes store here
        self.global_scope[ast.classname.name] = {}
        class_scope = {}

        # Check parent class
        if ast.parentname:
            if ast.parentname.name in self.global_scope:
                self.inheritance_map[ast.classname.name] = ast.parentname.name  
            else:
                raise Undeclared(Class(),ast.parentname.name)
        else: 
            self.inheritance_map[ast.classname.name] = "No super class"
        
        # Set up current class
        self.cur_cls = ast.classname.name
        ret_value = True
        if ast.classname.name != "Program":
            ret_value = False
        
        for mem in ast.memlist:
            if ret_value and isinstance(mem, MethodDecl) and ast.classname.name == "Program" and mem.name.name == "main":
                if len(mem.param) == 0:
                    ret_value = False
                    self.is_program_main_cls = True
                else:
                    return True
            
            self.visit(mem, class_scope)
            self.is_program_main_cls = False
            
        self.global_scope[ast.classname.name][CLASS_ATTRIBUTES] = class_scope
        
        return ret_value


    def visitAttributeDecl(self, ast: AttributeDecl, class_scope):
        self.visit(ast.decl, (class_scope, ast.kind))


    def visitMethodDecl(self,ast: MethodDecl, class_scope):
        if ast.name.name in self.global_scope[self.cur_cls]:
            raise Redeclared(Method(), ast.name.name) 
        

        
        is_inst = isinstance(ast.kind, Instance)
        param_type = list(map(lambda x: self.visit(x.varType, class_scope), ast.param))
        
        self.global_scope[self.cur_cls][ast.name.name] = type_for_checking("method", is_inst, None, param_type)

        self.cur_mth = ast.name.name
        param_mapping = {}
        for param in ast.param:
            self.visit(param, [param_mapping, Parameter()])

        class_scope[CURRENT_METHOD] = [param_mapping]
        self.visit(ast.body, [class_scope, 0])

        self.is_in_loop[0] = False
        self.cur_mth = None
        class_scope.pop(CURRENT_METHOD)


    def visitConstDecl(self, ast: ConstDecl, params):
        class_scope, kind = params
        if not ast.value: 
            raise IllegalConstantExpression(None)
        
        const_type = self.visit(ast.constType, class_scope)
        if CURRENT_METHOD in class_scope: # Có current method tức là đang trong 1 method.
            if ast.constant.name in class_scope[CURRENT_METHOD][kind]:
                raise Redeclared(Constant(), ast.constant.name)
            class_scope[CURRENT_METHOD][kind][ast.constant.name] = type_for_checking("const", 1, const_type)
        
        elif ast.constant.name in class_scope: # k có là đang ở trong class
            raise Redeclared(Attribute(), ast.constant.name)
        else:
            
            class_scope[ast.constant.name] = type_for_checking("const", 0 if isinstance(kind, Static) else 1, const_type)
        
        
        const_init_type = self.visit(ast.value, [class_scope, ast.value])
        if isinstance(const_init_type,type_for_checking):
            if const_init_type.obj_kind != "const":
                raise IllegalConstantExpression(ast.value)
            const_init_type = const_init_type.obj_type
        if not (Tools.compare_type_from_obj(const_init_type, const_type) or Tools.if_type_is_compatible(const_type, const_init_type, self.inheritance_map)):
            raise TypeMismatchInConstant(ast)


    def visitVarDecl(self, ast: VarDecl, params):
        class_scope, kind = params 
        var_type = self.visit(ast.varType, class_scope)
        assign_case = None
        if CURRENT_METHOD in class_scope: # Có current method tức là đang trong 1 method.
            if ast.variable.name in class_scope[CURRENT_METHOD][kind]:
                raise Redeclared(Variable(), ast.variable.name)
                   
            assign_case = 1
            
        
        elif isinstance(kind, Parameter):
            if ast.variable.name in class_scope:
                raise Redeclared(Parameter(), ast.variable.name)
            assign_case = 2
            

        elif ast.variable.name in class_scope: # k có là đang ở trong class
            raise Redeclared(Attribute(), ast.variable.name)
            # how about redeclare params same name with attributes
        
        else:
            assign_case = 3
            
        if ast.varInit:
            var_init_type = self.visit(ast.varInit, [class_scope, None])
            if isinstance(var_init_type,type_for_checking):
                var_init_type = var_init_type.obj_type
            if not (Tools.compare_type_from_obj(var_init_type, var_type) or Tools.if_type_is_compatible(var_type, var_init_type, self.inheritance_map)):
                raise TypeMismatchInConstant(ast)
        
        if assign_case == 1:
            class_scope[CURRENT_METHOD][kind][ast.variable.name] = type_for_checking("var", 1, var_type)
        elif assign_case == 2:
            class_scope[ast.variable.name] = type_for_checking("var", 1, var_type)
        elif assign_case == 3:
            class_scope[ast.variable.name] = type_for_checking("var", 0 if isinstance(kind, Static) else 1, var_type)

    
    def visitBlock(self, ast: Block, params):
        class_scope, num_block = params
        for instance in ast.inst:
            if isinstance(instance,Block):
                class_scope[CURRENT_METHOD].append({})
                self.visit(instance, [class_scope, num_block+1])
                class_scope[CURRENT_METHOD].pop()
            else:            
                self.visit(instance, [class_scope, num_block])


    def visitAssign(self,ast: Assign, params):
        lhs = self.visit(ast.lhs, params)
        if type(lhs) == type_for_checking:
            if lhs.obj_kind == "const":
                raise CannotAssignToConstant(ast)
            lhs = lhs.obj_type
        rhs = self.visit(ast.exp, params) if type(self.visit(ast.exp, params)) != type_for_checking else self.visit(ast.exp, params).obj_type
        if Tools.compare_type_from_obj(lhs, rhs) or Tools.if_type_is_compatible(lhs, rhs): return

        raise TypeMismatchInStatement(ast)


    def visitIf(self, ast: If, params):
        class_scope, num = params
        expr_type = self.visit(ast.expr, params)
        if isinstance(expr_type, type_for_checking):
            expr_type = expr_type.obj_type
        if not isinstance(expr_type, BoolType):
            raise TypeMismatchInStatement(self.if_statement if self.if_statement else ast)
        
        back_up = None
        back_up, self.if_statement = self.if_statement, back_up
        
        class_scope[CURRENT_METHOD].append({})
        self.visit(ast.thenStmt, [class_scope, num+1])
        class_scope[CURRENT_METHOD].pop()

        back_up, self.if_statement = self.if_statement, back_up

        if not isinstance(ast.elseStmt, If):
            self.if_statement = None
        elif not self.if_statement: 
            self.if_statement = ast
        if ast.elseStmt:
            class_scope[CURRENT_METHOD].append({})
            self.visit(ast.elseStmt, [class_scope, num+1])
            class_scope[CURRENT_METHOD].pop()

        self.if_statement = None      


    def visitFor(self,ast: For, params):
        class_scope, num = params
        self.is_in_loop[num+1] = True
        for_id = self.visit(ast.id, params)
        expr1 = self.visit(ast.expr1, params)
        expr2 = self.visit(ast.expr2, params)
        expr3 = self.visit(ast.expr3, params) if ast.expr3 else None

        if isinstance(expr1,type_for_checking):
            expr1 = expr1.obj_type
        
        if isinstance(expr2,type_for_checking):
            expr2 = expr2.obj_type
        
        if expr3 and isinstance(expr3,type_for_checking):
            expr3 = expr3.obj_type

        
        if (for_id.obj_kind == "const"): 
            raise CannotAssignToConstant(Assign(ast.id,ast.expr1))
        
        if (not isinstance(expr1, IntType) or not isinstance(expr2, IntType) or (expr3 and not isinstance(expr3, IntType))) or (type(for_id.obj_type) != IntType and type(for_id.obj_type) != FloatType):
            raise TypeMismatchInStatement(ast)
        
        class_scope[CURRENT_METHOD].append({})
        self.visit(ast.loop, [class_scope, num+1])
        class_scope[CURRENT_METHOD].pop()
        self.is_in_loop[num+1] = False


    def visitBreak(self, ast: Break, params):
        class_scope, num = params
        if num not in self.is_in_loop or not self.is_in_loop[num]:
            raise MustInLoop(ast)
        self.is_in_loop[num] = False
    
    def visitContinue(self, ast: Continue, params):
        class_scope, num = params
        if num not in self.is_in_loop or not self.is_in_loop[num]:
            raise MustInLoop(ast) 
        self.is_in_loop[num] = False

    def visitReturn(self, ast: Return, params):
        class_scope, num = params
        # Check for main method 
        if (self.cur_cls == "Program" and self.cur_mth == "main" and ast.expr) or self.cur_mth == "Destructor" or (self.cur_cls == "Constructor" and ast.expr): 
            raise TypeMismatchInStatement(ast)

        ret_type = self.visit(ast.expr, params) if ast.expr else VoidType()
        old_type = self.global_scope[self.cur_cls][self.cur_mth].obj_type
        if old_type:
            if Tools.compare_type_from_obj(old_type.obj_type, ret_type.obj_type) or Tools.if_type_is_compatible(old_type.obj_type, ret_type.obj_type):
                return 
            raise TypeMismatchInStatement(ast)
 
        self.global_scope[self.cur_cls][self.cur_mth].obj_type = ret_type

    
    def visitCallStmt(self,ast: CallStmt, params): # method access as statement (no lhs and rhs)
        class_scope, const_value = params
        # Self method
        if isinstance(ast.obj, SelfLiteral):
            if self.is_program_main_cls == False and self.cur_mth and self.global_scope[self.cur_cls][self.cur_mth].is_instance == False:
                raise IllegalMemberAccess(ast)
            
            call_mth_type = Tools.get_id_type_in_cur_scope(ast.method.name, self.global_scope[self.cur_cls])

            if call_mth_type == None or call_mth_type.obj_kind != "method":
                raise Undeclared(Method(), ast.method.name)
            
            if not call_mth_type.is_instance:
                raise IllegalMemberAccess(ast)
            
            if not isinstance(call_mth_type.obj_type, VoidType):
                raise TypeMismatchInStatement(ast)
            
            # check type of params
            param_type = list(map(lambda x: self.visit(x, params), ast.param))
            param_type = list(map(lambda x: x.obj_type if isinstance(x, type_for_checking) else x, param_type))
            if len(call_mth_type.method_param_type) != 0 and len(param_type) != 0 and not Tools.compare_paras_type_btwn_method_and_call(call_mth_type.method_param_type,param_type,self.inheritance_map):
                raise TypeMismatchInStatement(ast)
            
            return #call_mth_type.obj_type
        
        # Static method or local object_method call
        if isinstance(ast.obj, Id):
            if ast.method.name[0] == "$": # Static method
                if ast.obj.name not in self.global_scope:
                    raise IllegalMemberAccess(ast) if Tools.get_id_type_in_cur_scope(ast.obj.name, class_scope) else Undeclared(Class(), ast.obj.name)
                
                call_mth_type = Tools.get_field_type_of_class(ast.method.name, ast.obj.name, self.global_scope, True)

                if call_mth_type == None or call_mth_type.obj_kind != "method":
                    raise Undeclared(Method(), ast.method.name)
                
                if not isinstance(call_mth_type.obj_type, VoidType):
                    raise TypeMismatchInStatement(ast)
                
                # check type of params
                param_type = list(map(lambda x: self.visit(x, params), ast.param))
                param_type = list(map(lambda x: x.obj_type if isinstance(x, type_for_checking) else x, param_type))
                if len(call_mth_type.method_param_type) != 0 and len(param_type) != 0 and not Tools.compare_paras_type_btwn_method_and_call(call_mth_type.method_param_type,param_type,self.inheritance_map):
                    raise TypeMismatchInStatement(ast)
                
                return #call_mth_type.obj_type
            
            # Normal method call
            
            obj_type = Tools.get_id_type_in_cur_scope(ast.obj.name, class_scope[CURRENT_METHOD])
            if obj_type:
                if type(obj_type) == type_for_checking:
                    obj_type = obj_type.obj_type
                if type(obj_type) != ClassType:
                    raise IllegalMemberAccess(ast)
                call_mth_type = Tools.get_field_type_of_class(ast.method.name, obj_type.classname.name, self.global_scope, True)

                if call_mth_type == None or call_mth_type.obj_kind != "method":
                    raise Undeclared(Method(), ast.method.name)
                
                if not call_mth_type.is_instance:
                    raise IllegalMemberAccess(ast)
                
                if not isinstance(call_mth_type.obj_type, VoidType):
                    raise TypeMismatchInStatement(ast)
                
                # check type of params
                param_type = list(map(lambda x: self.visit(x, params), ast.param))
                param_type = list(map(lambda x: x.obj_type if isinstance(x, type_for_checking) else x, param_type))
                if len(call_mth_type.method_param_type) != 0 and len(param_type) != 0 and not Tools.compare_paras_type_btwn_method_and_call(call_mth_type.method_param_type,param_type,self.inheritance_map):
                    raise TypeMismatchInStatement(ast)
                
                return #call_mth_type.obj_type
            
            raise IllegalMemberAccess(ast) if ast.obj.name in self.global_scope else Undeclared(Identifier(), ast.obj.name)

        # ast.obj is Expr
        obj_type = self.visit(ast.obj, params)
        if type(obj_type) == type_for_checking:
            obj_type = obj_type.obj_type
        
        if not isinstance(obj_type,ClassType):
            raise TypeMismatchInStatement(ast)
        call_mth_type = Tools.get_field_type_of_class(ast.method.name,obj_type.classname.name,self.global_scope, True)

        if call_mth_type == None or call_mth_type.obj_kind != "method":
                raise Undeclared(Method(), ast.method.name)
                
        if not call_mth_type.is_instance:
            raise IllegalMemberAccess(ast)
                
        if not isinstance(call_mth_type.obj_type, VoidType):
            raise TypeMismatchInStatement(ast)
        
        if type(call_mth_type.obj_type) == VoidType:
            raise TypeMismatchInStatement(ast)
        
        param_type = list(map(lambda x: self.visit(x, params), ast.param))
        param_type = list(map(lambda x: x.obj_type if isinstance(x, type_for_checking) else x, param_type))
        if len(call_mth_type.method_param_type) != 0 and len(param_type) != 0 and not Tools.compare_paras_type_btwn_method_and_call(call_mth_type.method_param_type,param_type,self.inheritance_map):
            raise TypeMismatchInStatement(ast)
        
        #return call_mth_type.obj_type

    
    def visitArrayLiteral(self, ast: ArrayLiteral, params):
        class_scope, const_value = params
        change_array_lit = False
        if self.array_lit == None:
            self.array_lit = ast
            change_array_lit = True
        element_type = list(map(lambda x: self.visit(x, [class_scope, None]), ast.value))
        element_type = list(map(lambda x: x.obj_type if isinstance(x,type_for_checking) else x, element_type))
        ret_type = element_type[0]
        element_type = list(map(lambda x: Tools.compare_type_from_obj(x, element_type[0]), element_type))
        if reduce(lambda x, y: x == y == True, element_type):
            if change_array_lit == True:
                self.array_lit = None
            return ArrayType(len(element_type),ret_type)
        
        raise IllegalArrayLiteral(self.array_lit)
    
    
    def visitBinaryOp(self, ast: BinaryOp, params):
        ret_kind = "const"
        lhs_og = lhs = self.visit(ast.left, params) 
        rhs_og = rhs = self.visit(ast.right, params)
        if isinstance(lhs_og, type_for_checking):
            lhs = lhs.obj_type
        if isinstance(rhs_og, type_for_checking):
            rhs = rhs.obj_type
        if isinstance(lhs_og, type_for_checking) and isinstance(rhs_og, type_for_checking) and (lhs_og.obj_kind != "const" or rhs_og.obj_kind != "const"):
            ret_kind = "var"
        
        if ast.op in ["+", "-", "*", "/"]:
            if (isinstance(lhs, IntType) or isinstance(lhs, FloatType)) and (isinstance(rhs, FloatType) or isinstance(rhs,IntType)):
                ret_type = FloatType() if type(lhs) == FloatType or type(rhs) == FloatType or ast.op == "/" else IntType()
                return type_for_checking(ret_kind,1,ret_type)
            
            raise TypeMismatchInExpression(ast)
        
        elif ast.op == "%":
            if type(lhs) != IntType or type(rhs) != IntType:
                raise TypeMismatchInExpression(ast)
            return type_for_checking(ret_kind,1,IntType())

        elif ast.op in ["&&", "||"]:
            if type(lhs) != BoolType or type(rhs) != BoolType:
                raise TypeMismatchInExpression(ast)
            return type_for_checking(ret_kind,1,BoolType())
        
        elif ast.op == "==.":
            if type(lhs) != StringType or type(rhs) != StringType:
                raise TypeMismatchInExpression(ast)
            return type_for_checking(ret_kind,1,BoolType())
        
        elif ast.op == "+.":
            if type(lhs) != StringType or type(rhs) != StringType:
                raise TypeMismatchInExpression(ast)
            return type_for_checking(ret_kind,1,StringType())
        
        elif ast.op == "==" or ast.op == "!=":
            if (isinstance(lhs, BoolType) and isinstance(rhs, BoolType)) or (isinstance(lhs, IntType) and isinstance(rhs, IntType)):
                return type_for_checking(ret_kind,1,BoolType())
            
            raise TypeMismatchInExpression(ast)
        
        elif ast.op in ["<", ">", "<=", ">="]:
            if (type(lhs) != FloatType and type(lhs) != IntType) or (type(rhs) != FloatType and type(rhs) != IntType):
                raise TypeMismatchInExpression(ast)
            return type_for_checking(ret_kind,1,BoolType())


    def visitUnaryOp(self, ast: UnaryOp, params):
        ret_kind = "const"
        rhs = self.visit(ast.body, params) 
        if isinstance(rhs, type_for_checking):
            if rhs.obj_kind != "const": ret_kind = "var"
            rhs = rhs.obj_type

        if (ast.op == "!" and type(rhs) != BoolType) or (ast.op == "-" and type(rhs) != FloatType and type(rhs) != IntType):
            raise TypeMismatchInExpression(ast)
        
        return type_for_checking(ret_kind,1,rhs)


    def visitCallExpr(self, ast: CallExpr, params): # method access from rhs
        class_scope, const_value = params
        if type(const_value) == Expr: 
            raise IllegalConstantExpression(const_value)
        
        # Self method
        if isinstance(ast.obj, SelfLiteral):
            if self.is_program_main_cls == False and self.cur_mth and self.global_scope[self.cur_cls][self.cur_mth].is_instance == False:
                raise IllegalMemberAccess(ast)
            
            call_mth_type = Tools.get_id_type_in_cur_scope(ast.method.name, self.global_scope[self.cur_cls])

            if call_mth_type == None or call_mth_type.obj_kind != "method":
                raise Undeclared(Method(), ast.method.name)
            
            if not call_mth_type.is_instance:
                raise IllegalMemberAccess(ast)
            
            if isinstance(call_mth_type.obj_type, VoidType):
                raise TypeMismatchInExpression(ast)
            
            # check type of params
            param_type = list(map(lambda x: self.visit(x, params), ast.param))
            param_type = list(map(lambda x: x.obj_type if isinstance(x, type_for_checking) else x, param_type))
            if len(call_mth_type.method_param_type) != 0 and len(param_type) != 0 and not Tools.compare_paras_type_btwn_method_and_call(call_mth_type.method_param_type,param_type,self.inheritance_map):
                raise TypeMismatchInExpression(ast)
            
            return call_mth_type.obj_type
        
        # Static method or local object_method call
        if isinstance(ast.obj, Id):
            if ast.method.name[0] == "$": # Static method
                if ast.obj.name not in self.global_scope:
                    raise IllegalMemberAccess(ast) if Tools.get_id_type_in_cur_scope(ast.obj.name, class_scope) else Undeclared(Class(), ast.obj.name)
                
                call_mth_type = Tools.get_field_type_of_class(ast.method.name, ast.obj.name, self.global_scope, True)

                if call_mth_type == None or call_mth_type.obj_kind != "method":
                    raise Undeclared(Method(), ast.method.name)
                
                if isinstance(call_mth_type.obj_type, VoidType):
                    raise TypeMismatchInExpression(ast)
                
                # check type of params
                param_type = list(map(lambda x: self.visit(x, params), ast.param))
                param_type = list(map(lambda x: x.obj_type if isinstance(x, type_for_checking) else x, param_type))
                if len(call_mth_type.method_param_type) != 0 and len(param_type) != 0 and not Tools.compare_paras_type_btwn_method_and_call(call_mth_type.method_param_type,param_type,self.inheritance_map):
                    raise TypeMismatchInExpression(ast)
                
                return call_mth_type.obj_type
            
            # Normal method call
            
            obj_type = Tools.get_id_type_in_cur_scope(ast.obj.name, class_scope[CURRENT_METHOD])
            if obj_type:
                if type(obj_type) == type_for_checking:
                    obj_type = obj_type.obj_type
                if type(obj_type) != ClassType:
                    raise IllegalMemberAccess(ast)
                call_mth_type = Tools.get_field_type_of_class(ast.method.name, obj_type.classname.name, self.global_scope, True)

                if call_mth_type == None or call_mth_type.obj_kind != "method":
                    raise Undeclared(Method(), ast.method.name)
                
                if not call_mth_type.is_instance:
                    raise IllegalMemberAccess(ast)
                
                if isinstance(call_mth_type.obj_type, VoidType):
                    raise TypeMismatchInExpression(ast)
                
                # check type of params
                param_type = list(map(lambda x: self.visit(x, params), ast.param))
                param_type = list(map(lambda x: x.obj_type if isinstance(x, type_for_checking) else x, param_type))
                if len(call_mth_type.method_param_type) != 0 and len(param_type) != 0 and not Tools.compare_paras_type_btwn_method_and_call(call_mth_type.method_param_type,param_type,self.inheritance_map):
                    raise TypeMismatchInExpression(ast)
                
                return call_mth_type.obj_type
            
            raise IllegalMemberAccess(ast) if ast.obj.name in self.global_scope else Undeclared(Identifier(), ast.obj.name)

        # ast.obj is Expr
        obj_type = self.visit(ast.obj, params)
        if type(obj_type) == type_for_checking:
            obj_type = obj_type.obj_type
        if not isinstance(obj_type,ClassType):
            raise TypeMismatchInExpression(ast)
        call_mth_type = Tools.get_field_type_of_class(ast.method.name,obj_type.classname.name,self.global_scope, True)

        if call_mth_type == None or call_mth_type.obj_kind != "method":
                raise Undeclared(Method(), ast.method.name)
                
        if not call_mth_type.is_instance:
            raise IllegalMemberAccess(ast)
                
        if isinstance(call_mth_type.obj_type, VoidType):
            raise TypeMismatchInExpression(ast)
        
        if type(call_mth_type.obj_type) == VoidType:
            raise TypeMismatchInExpression(ast)
        
        param_type = list(map(lambda x: self.visit(x, params), ast.param))
        param_type = list(map(lambda x: x.obj_type if isinstance(x, type_for_checking) else x, param_type))
        if len(call_mth_type.method_param_type) != 0 and len(param_type) != 0 and not Tools.compare_paras_type_btwn_method_and_call(call_mth_type.method_param_type,param_type,self.inheritance_map):
            raise TypeMismatchInExpression(ast)
        
        return call_mth_type.obj_type
        
    
    def visitNewExpr(self,ast: NewExpr, params):
        if ast.classname.name not in self.global_scope:
            raise Undeclared(Class(), ast.classname.name)
        # Check custom constructor
        if len(ast.param):
            if "Constructor" not in self.global_scope[ast.classname.name]:
                raise Undeclared(Method(), "Constructor")
            
            constructor_method = self.global_scope[ast.classname.name]["Constructor"].method_param_type
            args = list(map(lambda x:self.visit(x, params),ast.param))
            args = list(map(lambda x: x.obj_type if isinstance(x,type_for_checking) else x,args))
            if not Tools.compare_paras_type_btwn_method_and_call(constructor_method,args,None):
                raise TypeMismatchInExpression(ast)
        
        return type_for_checking("const",1, ClassType(Id(ast.classname.name)))

    def visitArrayCell(self, ast: ArrayCell, params):
        arr_id_type = self.visit(ast.arr, params) 
        idx_type = list(map(lambda x: self.visit(x, params), ast.idx))
        obj_kind = arr_id_type.obj_kind if isinstance(arr_id_type, type_for_checking) else None
        obj_type = arr_id_type.obj_type if isinstance(arr_id_type, type_for_checking) else arr_id_type

        for idx in idx_type:
            check_idx = idx.obj_type if isinstance(idx,type_for_checking) else idx
            if isinstance(check_idx, IntType) and isinstance(obj_type, ArrayType):
                obj_type = obj_type.eleType
                continue        
            raise TypeMismatchInExpression(ast)
        
        return type_for_checking(obj_kind,None,obj_type) 

    def visitFieldAccess(self, ast: FieldAccess, params): # attributes access from lhs
        class_scope, const_value = params
        if isinstance(ast.obj, SelfLiteral):
            
            if self.is_program_main_cls == False and self.cur_mth and self.global_scope[self.cur_cls][self.cur_mth].obj_kind == "method" and not self.global_scope[self.cur_cls][self.cur_mth].is_instance:
                raise IllegalMemberAccess(ast)
            
            field_type = Tools.get_id_type_in_cur_scope(ast.fieldname.name, class_scope)

            if field_type:
                if field_type.is_instance == False:
                    # Class_name::$static
                    raise IllegalMemberAccess(ast) 
                if type(const_value) == Expr and field_type.obj_kind != "const":
                    raise IllegalConstantExpression(const_value)    
                return field_type
            
            raise Undeclared(Attribute(), ast.fieldname.name)

        if isinstance(ast.obj, Id):
            if ast.fieldname.name[0] == "$":
                if ast.obj.name not in self.global_scope:
                    raise IllegalMemberAccess(ast) if Tools.get_id_type_in_cur_scope(ast.obj.name, class_scope[CURRENT_METHOD]) or Tools.get_id_type_in_cur_scope(ast.obj.name, class_scope) else Undeclared(Class(), ast.obj.name)
                
                
                field_type = Tools.get_field_type_of_class(ast.fieldname.name, ast.obj.name, self.global_scope) if str(ast.obj.name) != str(self.cur_cls) else Tools.get_id_type_in_cur_scope(ast.fieldname.name, class_scope)

                if field_type == None or field_type.obj_kind == "method":
                    raise Undeclared(Attribute(), ast.fieldname.name)
                
                '''
                if field_type.is_instance: raise IllegalMemberAccess(ast): raise IllegalMemberAccess''' 
                # Làm thế méo nào mà 1 thằng có $ có thể làm instance được ????

                if const_value and field_type.obj_kind == "var":
                    raise IllegalConstantExpression(ast)
                
                return field_type
            
            # if normal id
            # E.x is local variable and cur_cls is subclass of class of E => True
            # else False

            # find variable declare in current method
            obj_type = Tools.get_id_type_in_cur_scope(ast.obj.name, class_scope[CURRENT_METHOD]) # find in current class and all super class
            if obj_type:
                if isinstance(obj_type, type_for_checking):
                    obj_type = obj_type.obj_type
                if not isinstance(obj_type, ClassType):
                    raise TypeMismatchInExpression(ast)
                
                if not Tools.check_class_inheritance(self.cur_cls,obj_type.classname.name,self.inheritance_map):
                    raise Undeclared(Attribute(), ast.fieldname.name)

                field_type = Tools.get_field_type_of_class(ast.fieldname.name, obj_type.classname.name, self.global_scope)

                if field_type is None or field_type.obj_kind == "method": 
                    raise Undeclared(Attribute(), ast.fieldname.name)

                if not field_type.is_instance:
                    raise IllegalMemberAccess(ast)
                
                if const_value and field_type.obj_kind == "var":
                    raise IllegalConstantExpression(const_value)
                
                return field_type

            raise IllegalMemberAccess(ast) if ast.obj.name in self.global_scope else Undeclared(Identifier(), ast.obj.name)
        
        #obj is an expression
        field_kind = "const"
        obj_type = obj_type_og = self.visit(ast.obj, params)
        if isinstance(obj_type_og, type_for_checking):
            obj_type = obj_type_og.obj_type
            if obj_type_og.obj_kind != "const":
                field_kind = "var"
        if not isinstance(obj_type, ClassType):
            raise TypeMismatchInExpression(ast)
        
        
        field_type = Tools.get_field_type_of_class(ast.fieldname.name, obj_type.classname.name, self.global_scope)

        if field_type is None or field_type.obj_kind == "method": 
            raise Undeclared(Attribute(), ast.fieldname.name)

        if not field_type.is_instance:
            raise IllegalMemberAccess(ast)
                
        if const_value and field_type.obj_kind == "var":
            raise IllegalConstantExpression(const_value)

        if field_type.obj_kind != "const": field_kind = "var"    
        return type_for_checking(field_kind,1,field_type.obj_type)
        


    def visitId(self, ast: Id, params):
        class_scope, const_value = params
        
        if CURRENT_METHOD in class_scope:
            the_id = Tools.get_id_type_in_cur_scope(ast.name, class_scope[CURRENT_METHOD])
            if the_id:
                return the_id
            
        raise Undeclared(Identifier(), ast.name)


    def visitIntType(self, ast, _):
        return ast

    def visitFloatType(self, ast, _):
        return ast
    
    def visitBoolType(self, ast, _):
        return ast
    
    def visitStringType(self, ast, _):
        return ast

    def visitArrayType(self, ast, _):
        return ast
    
    def visitClassType(self, ast: ClassType, _):
        if ast.classname.name not in self.global_scope:
            raise Undeclared(Class(), ast.classname.name)
        return ast

    def visitIntLiteral(self, ast, _):
        return type_for_checking("const",1,IntType())
    
    def visitFloatLiteral(self, ast, _):
        return type_for_checking("const",1,FloatType())
    
    def visitStringLiteral(self, ast, _):
        return type_for_checking("const",1,StringType())
    
    def visitBooleanLiteral(self, ast, _):
        return type_for_checking("const",1, BoolType())
    
    def visitNullLiteral(self, ast: NullLiteral, _):
        return type_for_checking("const",1,ast)
    
    def visitSelfLiteral(self, ast, _):
        return ast
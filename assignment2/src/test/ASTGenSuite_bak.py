import unittest
from TestUtils import TestAST
from AST import *
#from main.d96.utils.AST import *

class ASTGenSuite(unittest.TestCase):
    def test__300_simple_program(self):
        str_in = """Class Program {}"""
        expect = """Program([ClassDecl(Id(Program),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,300))

    def test_301_simple_program_2(self):
        str_in = """Class Program : Computer {}"""
        expect = """Program([ClassDecl(Id(Program),Id(Computer),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,301))
    
    def test_302_simple_program_3(self):
        str_in = """Class Program {
            Constructor(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,302))
    
    def test_303_simple_program_4(self):
        str_in = """Class Program {
            Destructor(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,303))
    
    def test_304_simple_program_5(self):
        str_in = """Class Program {
            Main(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Main),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,304))
    
    def test_305_simple_program_6(self):
        str_in = """Class Program {
            $Main(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($Main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,305))
    
    def test__306_simple_program_double(self):
        str_in = """Class Program {}
                    Class Foo {}"""
        expect = """Program([ClassDecl(Id(Program),[]),ClassDecl(Id(Foo),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,306))

    def test_307_simple_program_double_2(self):
        str_in = """Class Program : Computer {}
                    Class Foo : TheFoo {}"""
        expect = """Program([ClassDecl(Id(Program),Id(Computer),[]),ClassDecl(Id(Foo),Id(TheFoo),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,307))
    
    def test_308_simple_program_double_3(self):
        str_in = """Class Program {
            Constructor(){}
            Constructor(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,308))
    
    def test_309_simple_program_double_4(self):
        str_in = """Class Program {
            Destructor(){}
            Constructor(){}
            Destructor(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,309))
    
    def test_310_simple_program_double_5(self):
        str_in = """Class Program {
            Main(){}
            Foo(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Main),Instance,[],Block([])),MethodDecl(Id(Foo),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,310))
    
    def test_311_simple_program_double_6(self):
        str_in = """Class Program {
            $Main(){}
            $Foo(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($Main),Static,[],Block([])),MethodDecl(Id($Foo),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,311))
    
    def test_312_simple_program_7(self):
        str_in = """Class Program {
            Var a: Int;
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])"""
        self.assertTrue(TestAST.test(str_in,expect,312))
    
    def test_313_simple_program_8(self):
        str_in = """Class Program {
            Var a: Int = 3;
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(3)))])])"""
        self.assertTrue(TestAST.test(str_in,expect,313))
    
    def test_314_simple_program_9(self):
        str_in = """Class Program {
            Val a: Int = 3;
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(3)))])])"""
        self.assertTrue(TestAST.test(str_in,expect,314))
    
    def test_315_simple_program_10(self):
        str_in = """Class Program {
            $Main(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($Main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,315))
    
    def test__316_simple_program_11(self):
        str_in = """
Class Program {
    main () {
        a.putIntLn(4);
    }
}"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(a),Id(putIntLn),[IntLit(4)])]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,316))

    def test_317_simple_program_triple(self):
        str_in = """
Class Program {}
Class Bullshit{}
Class RapGod{}"""
        expect = """Program([ClassDecl(Id(Program),[]),ClassDecl(Id(Bullshit),[]),ClassDecl(Id(RapGod),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,317))
    
    def test_318_logical_expr(self):
        str_in = """
Class Program {
    method_full(x, y: Int; z: String) {}
    main () {
        a = a && b && b && b;
        a = c || d || d || d;
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method_full),Instance,[param(Id(x),IntType),param(Id(y),IntType),param(Id(z),StringType)],Block([])),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(&&,BinaryOp(&&,BinaryOp(&&,Id(a),Id(b)),Id(b)),Id(b))),AssignStmt(Id(a),BinaryOp(||,BinaryOp(||,BinaryOp(||,Id(c),Id(d)),Id(d)),Id(d)))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,318))
    
    def test_319_simple_program_double_4(self):
        str_in = """
Class Program {}
Class Bullshit : someShit{}
Class RapGod{}
        """
        expect = """Program([ClassDecl(Id(Program),[]),ClassDecl(Id(Bullshit),Id(someShit),[]),ClassDecl(Id(RapGod),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,319))
    
    def test__320_simple_program(self):
        str_in = """Class Program {}"""
        expect = """Program([ClassDecl(Id(Program),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,320))

    def test_321_mix_program_2(self):
        str_in = """
Class Program {
    main(){}
    getProcInfo(){}
}
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(getProcInfo),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,321))
    
    def test_322_simple_program_3(self):
        str_in = """Class Program {
            Constructor(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,322))
    
    def test_323_mix_program_4(self):
        str_in = """
Class Program {
    getProcInfo(){}
    $showProcInfo(){}
}
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(getProcInfo),Instance,[],Block([])),MethodDecl(Id($showProcInfo),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,323))
    
    def test_324_new_expr(self):
        str_in = """
Class Program {
    main () {
        a = New class(1+2-3*4/5%6&&7||8, a[9][10][11], a.a.a, a.method(), a::$a, a::$method());
        a = New class(New class(New class(1,2,(3).a)));
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(class),[BinaryOp(||,BinaryOp(&&,BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(%,BinaryOp(/,BinaryOp(*,IntLit(3),IntLit(4)),IntLit(5)),IntLit(6))),IntLit(7)),IntLit(8)),ArrayCell(Id(a),[IntLit(9),IntLit(10),IntLit(11)]),FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),CallExpr(Id(a),Id(method),[]),FieldAccess(Id(a),Id($a)),CallExpr(Id(a),Id($method),[])])),AssignStmt(Id(a),NewExpr(Id(class),[NewExpr(Id(class),[NewExpr(Id(class),[IntLit(1),IntLit(2),FieldAccess(IntLit(3),Id(a))])])]))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,324))
    
    def test_325_simple_program_6(self):
        str_in = """
Class Program {
    Val temp: Float = 2.3;
}
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(temp),FloatType,FloatLit(2.3)))])])"""
        self.assertTrue(TestAST.test(str_in,expect,325))
    
    def test__326_simple_program_double(self):
        str_in = """Class Program {}
                    Class Foo {}"""
        expect = """Program([ClassDecl(Id(Program),[]),ClassDecl(Id(Foo),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,326))

    def test_327_simple_program_double_2(self):
        str_in = """
Class Program{
    Var bruh, bruh2, bruh3: Boolean = a,b,c;
}
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(bruh),BoolType,Id(a))),AttributeDecl(Instance,VarDecl(Id(bruh2),BoolType,Id(b))),AttributeDecl(Instance,VarDecl(Id(bruh3),BoolType,Id(c)))])])"""
        self.assertTrue(TestAST.test(str_in,expect,327))
    
    def test_328_mul_expr(self):
        str_in = """
Class Program {
    main () {
        a = 2 / 1;
        a = 2 * 1;
        a = 3 % 2;
    }   
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(/,IntLit(2),IntLit(1))),AssignStmt(Id(a),BinaryOp(*,IntLit(2),IntLit(1))),AssignStmt(Id(a),BinaryOp(%,IntLit(3),IntLit(2)))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,328))
    
    def test_329_method_declare(self):
        str_in = """
Class Program {
    method_full(x, y: Int; z: String) {}
    main () {}
}
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method_full),Instance,[param(Id(x),IntType),param(Id(y),IntType),param(Id(z),StringType)],Block([])),MethodDecl(Id(main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,329))
    
    def test_330_simple_program_double_5(self):
        str_in = """Class Program {
            Main(){}
            Foo(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Main),Instance,[],Block([])),MethodDecl(Id(Foo),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,330))
    
    def test_331_method_decl(self):
        str_in = """
Class Program {
    $method_full(x, y: Int; z: String) {}
    $foo_method(){}
    main () {}
}
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($method_full),Static,[param(Id(x),IntType),param(Id(y),IntType),param(Id(z),StringType)],Block([])),MethodDecl(Id($foo_method),Static,[],Block([])),MethodDecl(Id(main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,331))
    
    def test_332_simple_program_7(self):
        str_in = """
Class Program{
    main () {
        a::$a = "foo" || "foo" && "foo" * 0 / 0x0 % (a  + a.a + class::$a- a.a() - class::$a());
        a::$a.a = "foo" || "foo" && "foo" * 0 / 0x0 % (a  + a.a + class::$a- a.a() - class::$a());
        a[1][1][1] = "foo" || "foo" && "foo" * 0 / 0x0 % (a + a.a + class::$a- a.a() - class::$a());
        a[a[a[a[1]]]][a[a[a]]] = "foo" || "foo" && "foo" * 0 / 0x0 % (a + a.a + class::$a- a.a() - class::$a());
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(a),Id($a)),BinaryOp(&&,BinaryOp(||,StringLit(foo),StringLit(foo)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(foo),IntLit(0)),IntLit(0)),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(class),Id($a))),CallExpr(Id(a),Id(a),[])),CallExpr(Id(class),Id($a),[]))))),AssignStmt(FieldAccess(FieldAccess(Id(a),Id($a)),Id(a)),BinaryOp(&&,BinaryOp(||,StringLit(foo),StringLit(foo)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(foo),IntLit(0)),IntLit(0)),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(class),Id($a))),CallExpr(Id(a),Id(a),[])),CallExpr(Id(class),Id($a),[]))))),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1),IntLit(1)]),BinaryOp(&&,BinaryOp(||,StringLit(foo),StringLit(foo)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(foo),IntLit(0)),IntLit(0)),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(class),Id($a))),CallExpr(Id(a),Id(a),[])),CallExpr(Id(class),Id($a),[]))))),AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])]),ArrayCell(Id(a),[ArrayCell(Id(a),[Id(a)])])]),BinaryOp(&&,BinaryOp(||,StringLit(foo),StringLit(foo)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(foo),IntLit(0)),IntLit(0)),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(class),Id($a))),CallExpr(Id(a),Id(a),[])),CallExpr(Id(class),Id($a),[])))))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,332))
    
    def test_333_simple_program_8(self):
        str_in = """
Class Program{
    Var $k98, $k99: Int = 98, 99;
    main () {
        Var k100: Boolean = True;
    }
}
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,VarDecl(Id($k98),IntType,IntLit(98))),AttributeDecl(Static,VarDecl(Id($k99),IntType,IntLit(99))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(k100),BoolType,BooleanLit(True))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,333))
    
    def test_334_adding_expr(self):
        str_in = """
Class Program {
    $method_full(x, y: Int; z: String) {}
    main () {
        a = a + b;
        a = a - b;
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($method_full),Static,[param(Id(x),IntType),param(Id(y),IntType),param(Id(z),StringType)],Block([])),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(+,Id(a),Id(b))),AssignStmt(Id(a),BinaryOp(-,Id(a),Id(b)))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,334))
    
    def test_335_simple_program_6(self):
        str_in = """
Class Program{
    Var a: Array[Int, 5];
    Val b: Array[Float, 0xABEF];
    Val _c: Array[String, 0b1011];
    Var $d: Array[Int, 07654];
}
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(44015,FloatType),None)),AttributeDecl(Instance,ConstDecl(Id(_c),ArrayType(11,StringType),None)),AttributeDecl(Static,VarDecl(Id($d),ArrayType(4012,IntType)))])])"""
        self.assertTrue(TestAST.test(str_in,expect,335))
    
    def test__336_simple_program_double(self):
        str_in = """Class Program {}
                    Class Foo {}"""
        expect = """Program([ClassDecl(Id(Program),[]),ClassDecl(Id(Foo),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,336))

    def test_337_simple_program_double_2(self):
        str_in = """
Class Program {
    Var list: Array[Int, 3] = Array(1, 1.1e-3, someClass.method(), Self.x, "foo", class::$y);
}        
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(list),ArrayType(3,IntType),[IntLit(1),FloatLit(0.0011),CallExpr(Id(someClass),Id(method),[]),FieldAccess(Self(),Id(x)),StringLit(foo),FieldAccess(Id(class),Id($y))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,337))
    
    def test_338_adding_expr(self):
        str_in = """
Class Program {
    Var $k98, $k99: Int = 98, 99;
    main () {
        a = 1 + 2 - 3 + 4 - 5 + 6 - 7;
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,VarDecl(Id($k98),IntType,IntLit(98))),AttributeDecl(Static,VarDecl(Id($k99),IntType,IntLit(99))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,BinaryOp(-,BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6)),IntLit(7)))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,338))
    
    def test_339_multi_dimension_array_decl(self):
        str_in = """
Class Program{
    Val list_String: Array[Array[String, 3], 3] 
    = Array(
        Array("a","b","c"),
        Array("a","b","c"),
        Array("a","b","c")
    );  
}
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(list_String),ArrayType(3,ArrayType(3,StringType)),[[StringLit(a),StringLit(b),StringLit(c)],[StringLit(a),StringLit(b),StringLit(c)],[StringLit(a),StringLit(b),StringLit(c)]]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,339))
    
    def test__340_simple_program(self):
        str_in = """Class Program {}"""
        expect = """Program([ClassDecl(Id(Program),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,340))

    def test_341_multi_demension_array(self):
        str_in = """
Class Program {
    Val list_String, str: Array[Array[String, 3], 3] 
    = Array(
        Array("a","b","c"),
        Array("a","b","c"),
        Array("a","b","c")
    ),Array(
        Array("a","b","c"),
        Array("a","b","c"),
        Array("a","b","c")
    );  
}
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(list_String),ArrayType(3,ArrayType(3,StringType)),[[StringLit(a),StringLit(b),StringLit(c)],[StringLit(a),StringLit(b),StringLit(c)],[StringLit(a),StringLit(b),StringLit(c)]])),AttributeDecl(Instance,ConstDecl(Id(str),ArrayType(3,ArrayType(3,StringType)),[[StringLit(a),StringLit(b),StringLit(c)],[StringLit(a),StringLit(b),StringLit(c)],[StringLit(a),StringLit(b),StringLit(c)]]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,341))
    
    def test_342_simple_program_3(self):
        str_in = """
Class Program{
    Val $k: Array[Int, 3] = Array(0/17%5, !-230, 1+2-3/4, a.method()[3]);
}
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($k),ArrayType(3,IntType),[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5)),UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)])]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,342))
    
    def test_343_new_expr(self):
        str_in = """
Class Program {
    main () {
        a = New class();
        a = New class(1,2);
        a = New class().b;
        a = New class()[a][b][c];
        a = (New class()).a.a.a;
        a = (New class())[a][b][c];
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(class),[])),AssignStmt(Id(a),NewExpr(Id(class),[IntLit(1),IntLit(2)])),AssignStmt(Id(a),FieldAccess(NewExpr(Id(class),[]),Id(b))),AssignStmt(Id(a),ArrayCell(NewExpr(Id(class),[]),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(class),[]),Id(a)),Id(a)),Id(a))),AssignStmt(Id(a),ArrayCell(NewExpr(Id(class),[]),[Id(a),Id(b),Id(c)]))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,343))
    
    def test_344_simple_program_5(self):
        str_in = """
Class Program {
    Val $k: Array[Int, 3] = Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11);
}"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($k),ArrayType(3,IntType),[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,344))
    
    def test_345_simple_program_6(self):
        str_in = """Class Program {
            $Main(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($Main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,345))
    
    def test__346_multi_demension_array_lit(self):
        str_in = """
Class Program {
    Val $k: Array[Int, 3] 
    = Array(
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11)
    );
    Val $k: Array[Int, 3] 
    = Array(
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11)
    );
}        
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($k),ArrayType(3,IntType),[[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))],[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))],[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))]])),AttributeDecl(Static,ConstDecl(Id($k),ArrayType(3,IntType),[[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))],[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))],[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))]]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,346))

    def test_347_mul_expr(self):
        str_in = """
Class Program {
    main () {
        a = 2 / 3 * 4 % 5 % 5 * (4 - 3 / 2);
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(*,BinaryOp(%,BinaryOp(%,BinaryOp(*,BinaryOp(/,IntLit(2),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(5)),BinaryOp(-,IntLit(4),BinaryOp(/,IntLit(3),IntLit(2)))))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,347))
    
    def test_348_simple_program_double_3(self):
        str_in = """
Class Program {
    Val $k, l, m, n: Array[Int, 3] 
    = Array(
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11)
    ),
    Array(
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11)
    ),
    Array(
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11)
    ),
    Array(
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11),
        Array(Array(0/17%5), !-230, 1+2-3/4, a.method()[3]-11)
    );
}"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($k),ArrayType(3,IntType),[[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))],[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))],[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))]])),AttributeDecl(Instance,ConstDecl(Id(l),ArrayType(3,IntType),[[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))],[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))],[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))]])),AttributeDecl(Instance,ConstDecl(Id(m),ArrayType(3,IntType),[[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))],[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))],[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))]])),AttributeDecl(Instance,ConstDecl(Id(n),ArrayType(3,IntType),[[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))],[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))],[[BinaryOp(%,BinaryOp(/,IntLit(0),IntLit(17)),IntLit(5))],UnaryOp(!,UnaryOp(-,IntLit(230))),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(-,ArrayCell(CallExpr(Id(a),Id(method),[]),[IntLit(3)]),IntLit(11))]]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,348))
    
    def test_349_simple_program_double_4(self):
        str_in = """Class Program {
            Destructor(){}
            Constructor(){}
            Destructor(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,349))
    
    def test_350_simple_program_double_5(self):
        str_in = """
Class Program{
    Var b: Array[Array[Array[Array[Int, 3], 3], 3], 3]
    = Array(
        Array(
            Array(
                Array("nothing here")
            )
        )
    );
}        
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(b),ArrayType(3,ArrayType(3,ArrayType(3,ArrayType(3,IntType)))),[[[[StringLit(nothing here)]]]]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,350))
    
    def test_351_simple_program_double_6(self):
        str_in = """
Class Program {
    Var list: Array[Array[Array[Array[Int,1],1],1],2];
    Var list: Int = Array (
        Array (
            Array (
                "bruh"
            ),
            Array (
                "bruh"
            )
        ),
        Array (
            Array (
                "bruh"
            ),
            Array (
                "bruh"
            )
        )
    );
    Var array: Array[Array[Array[Array[Int,1],1],1],1];
}        
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(list),ArrayType(2,ArrayType(1,ArrayType(1,ArrayType(1,IntType)))))),AttributeDecl(Instance,VarDecl(Id(list),IntType,[[[StringLit(bruh)],[StringLit(bruh)]],[[StringLit(bruh)],[StringLit(bruh)]]])),AttributeDecl(Instance,VarDecl(Id(array),ArrayType(1,ArrayType(1,ArrayType(1,ArrayType(1,IntType))))))])])"""
        self.assertTrue(TestAST.test(str_in,expect,351))
    
    def test_352_simple_program_7(self):
        str_in = """Class Program {
            Var a: Int;
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])"""
        self.assertTrue(TestAST.test(str_in,expect,352))
    
    def test_353_simple_program_constructor(self):
        str_in = """
Class Program {
    Constructor(x, y: Int; z, q: Float){
        x = x;
        y = y;
    }
    Destructor(){
        z = z;
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType),param(Id(z),FloatType),param(Id(q),FloatType)],Block([AssignStmt(Id(x),Id(x)),AssignStmt(Id(y),Id(y))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(z),Id(z))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,353))
    
    def test_354_simple_program_9(self):
        str_in = """Class Program {
            Val a: Int = 3;
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(3)))])])"""
        self.assertTrue(TestAST.test(str_in,expect,354))
    
    def test_355_simple_program_6(self):
        str_in = """
Class Program {
    main () {
        Var a: Array[Int, 2] = Array();
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(2,IntType),[])]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,355))
    
    def test__356_simple_program_double(self):
        str_in = """Class Program {}
                    Class Foo {}"""
        expect = """Program([ClassDecl(Id(Program),[]),ClassDecl(Id(Foo),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,356))

    def test_357_simple_program_double_2(self):
        str_in = """
Class Program{
    Val $c: Float;
    main () {
        Var a,b: Int = 1, 1+2;
        Val a,b,c,d: Int = 1, 1+2,3,4;
        Var a,b,e,f,g,h,i,k,l,m: Int = 1, 1+2, 3,4,5,6,7,8,9,0;
    }   
}        
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($c),FloatType,None)),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(1)),VarDecl(Id(b),IntType,BinaryOp(+,IntLit(1),IntLit(2))),ConstDecl(Id(a),IntType,IntLit(1)),ConstDecl(Id(b),IntType,BinaryOp(+,IntLit(1),IntLit(2))),ConstDecl(Id(c),IntType,IntLit(3)),ConstDecl(Id(d),IntType,IntLit(4)),VarDecl(Id(a),IntType,IntLit(1)),VarDecl(Id(b),IntType,BinaryOp(+,IntLit(1),IntLit(2))),VarDecl(Id(e),IntType,IntLit(3)),VarDecl(Id(f),IntType,IntLit(4)),VarDecl(Id(g),IntType,IntLit(5)),VarDecl(Id(h),IntType,IntLit(6)),VarDecl(Id(i),IntType,IntLit(7)),VarDecl(Id(k),IntType,IntLit(8)),VarDecl(Id(l),IntType,IntLit(9)),VarDecl(Id(m),IntType,IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,357))
    
    def test_358_simple_program_double_3(self):
        str_in = """Class Program {
            Constructor(){}
            Constructor(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,358))
    
    def test_359_simple_program_double_4(self):
        str_in = """
Class Program {
    main() {
        Var a: Int = Array(1,2,3);
        a = Array(1,2,3);
        a = 1234;
        a = 0X123F;
        a = 0b1111;
        a = 07654;
        a = 0XAAAA + 0b1000 - 0357 * 9999 / 3.1e27;
        class::$a = Array(1,2,3);
        class::$a = 1234;
        class::$a = 0X123F;
        class::$a = 0b1111;
        class::$a = 07654;
        class::$a = 0XAAAA + 0b1000 - 0357 * 9999 / 3.1e27; 
        class.a = Array(1,2,3);
        class.a = 1234;
        class.a = 0X123F;
        class.a = 0b1111;
        Self.a = 07654;
        class.a = 0XAAAA + 0b1000 - 0357 * 9999 / 3.1e27;

        foo_var = 1 - 2 && 3 * 4 || 4 + 5;
        foo_var = True + False && False - True && (True && False - True && 0B1111111);
        foo_var = True + False || False - True && (True || False - True || 0B1111111);

        class.foo_var = 1 - 2 && 3 * 4 || 4 + 5;
        class.foo_var = True + False && False - True && (True && False - True && 0B1111111);
        class::$foo_var = True + False || False - True || (True || False - True || 0B1111111);

        foo_arr[125] = a[b[c[3]]];
        foo_arr[125][123][123] = a[b[c[3]]][6][6][6][9];
        foo_arr[125][123][123] = a[b[c[3]]][6][6][6][9] + foo.class().bc(bc)[5][6][7];

        class.foo_arr[125] = a[b[c[3]]];
        class.foo_arr[125][123][123] = a[b[c[3]]][6][6][6][9];
        class::$foo_arr[125][123][123] = a[b[c[3]]][6][6][6][9] + foo.class().bc(bc)[5][6][7];

        a.a.a = 1;
        a::$a = 1;
        a[a] = 1;
        a[a[a[a[a[1]]]]][a[a[1]]] = 1;

        class::$a.a.a[class::$a[1]][class.a[1]] = 1;
        Self.a = 1;
        Self.a.a.a = 1;
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,[IntLit(1),IntLit(2),IntLit(3)]),AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),AssignStmt(Id(a),IntLit(1234)),AssignStmt(Id(a),IntLit(4671)),AssignStmt(Id(a),IntLit(15)),AssignStmt(Id(a),IntLit(4012)),AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,IntLit(43690),IntLit(8)),BinaryOp(/,BinaryOp(*,IntLit(239),IntLit(9999)),FloatLit(3.1e+27)))),AssignStmt(FieldAccess(Id(class),Id($a)),[IntLit(1),IntLit(2),IntLit(3)]),AssignStmt(FieldAccess(Id(class),Id($a)),IntLit(1234)),AssignStmt(FieldAccess(Id(class),Id($a)),IntLit(4671)),AssignStmt(FieldAccess(Id(class),Id($a)),IntLit(15)),AssignStmt(FieldAccess(Id(class),Id($a)),IntLit(4012)),AssignStmt(FieldAccess(Id(class),Id($a)),BinaryOp(-,BinaryOp(+,IntLit(43690),IntLit(8)),BinaryOp(/,BinaryOp(*,IntLit(239),IntLit(9999)),FloatLit(3.1e+27)))),AssignStmt(FieldAccess(Id(class),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),AssignStmt(FieldAccess(Id(class),Id(a)),IntLit(1234)),AssignStmt(FieldAccess(Id(class),Id(a)),IntLit(4671)),AssignStmt(FieldAccess(Id(class),Id(a)),IntLit(15)),AssignStmt(FieldAccess(Self(),Id(a)),IntLit(4012)),AssignStmt(FieldAccess(Id(class),Id(a)),BinaryOp(-,BinaryOp(+,IntLit(43690),IntLit(8)),BinaryOp(/,BinaryOp(*,IntLit(239),IntLit(9999)),FloatLit(3.1e+27)))),AssignStmt(Id(foo_var),BinaryOp(||,BinaryOp(&&,BinaryOp(-,IntLit(1),IntLit(2)),BinaryOp(*,IntLit(3),IntLit(4))),BinaryOp(+,IntLit(4),IntLit(5)))),AssignStmt(Id(foo_var),BinaryOp(&&,BinaryOp(&&,BinaryOp(+,BooleanLit(True),BooleanLit(False)),BinaryOp(-,BooleanLit(False),BooleanLit(True))),BinaryOp(&&,BinaryOp(&&,BooleanLit(True),BinaryOp(-,BooleanLit(False),BooleanLit(True))),IntLit(127)))),AssignStmt(Id(foo_var),BinaryOp(&&,BinaryOp(||,BinaryOp(+,BooleanLit(True),BooleanLit(False)),BinaryOp(-,BooleanLit(False),BooleanLit(True))),BinaryOp(||,BinaryOp(||,BooleanLit(True),BinaryOp(-,BooleanLit(False),BooleanLit(True))),IntLit(127)))),AssignStmt(FieldAccess(Id(class),Id(foo_var)),BinaryOp(||,BinaryOp(&&,BinaryOp(-,IntLit(1),IntLit(2)),BinaryOp(*,IntLit(3),IntLit(4))),BinaryOp(+,IntLit(4),IntLit(5)))),AssignStmt(FieldAccess(Id(class),Id(foo_var)),BinaryOp(&&,BinaryOp(&&,BinaryOp(+,BooleanLit(True),BooleanLit(False)),BinaryOp(-,BooleanLit(False),BooleanLit(True))),BinaryOp(&&,BinaryOp(&&,BooleanLit(True),BinaryOp(-,BooleanLit(False),BooleanLit(True))),IntLit(127)))),AssignStmt(FieldAccess(Id(class),Id($foo_var)),BinaryOp(||,BinaryOp(||,BinaryOp(+,BooleanLit(True),BooleanLit(False)),BinaryOp(-,BooleanLit(False),BooleanLit(True))),BinaryOp(||,BinaryOp(||,BooleanLit(True),BinaryOp(-,BooleanLit(False),BooleanLit(True))),IntLit(127)))),AssignStmt(ArrayCell(Id(foo_arr),[IntLit(125)]),ArrayCell(Id(a),[ArrayCell(Id(b),[ArrayCell(Id(c),[IntLit(3)])])])),AssignStmt(ArrayCell(Id(foo_arr),[IntLit(125),IntLit(123),IntLit(123)]),ArrayCell(Id(a),[ArrayCell(Id(b),[ArrayCell(Id(c),[IntLit(3)])]),IntLit(6),IntLit(6),IntLit(6),IntLit(9)])),AssignStmt(ArrayCell(Id(foo_arr),[IntLit(125),IntLit(123),IntLit(123)]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[ArrayCell(Id(c),[IntLit(3)])]),IntLit(6),IntLit(6),IntLit(6),IntLit(9)]),ArrayCell(CallExpr(CallExpr(Id(foo),Id(class),[]),Id(bc),[Id(bc)]),[IntLit(5),IntLit(6),IntLit(7)]))),AssignStmt(ArrayCell(FieldAccess(Id(class),Id(foo_arr)),[IntLit(125)]),ArrayCell(Id(a),[ArrayCell(Id(b),[ArrayCell(Id(c),[IntLit(3)])])])),AssignStmt(ArrayCell(FieldAccess(Id(class),Id(foo_arr)),[IntLit(125),IntLit(123),IntLit(123)]),ArrayCell(Id(a),[ArrayCell(Id(b),[ArrayCell(Id(c),[IntLit(3)])]),IntLit(6),IntLit(6),IntLit(6),IntLit(9)])),AssignStmt(ArrayCell(FieldAccess(Id(class),Id($foo_arr)),[IntLit(125),IntLit(123),IntLit(123)]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[ArrayCell(Id(c),[IntLit(3)])]),IntLit(6),IntLit(6),IntLit(6),IntLit(9)]),ArrayCell(CallExpr(CallExpr(Id(foo),Id(class),[]),Id(bc),[Id(bc)]),[IntLit(5),IntLit(6),IntLit(7)]))),AssignStmt(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),IntLit(1)),AssignStmt(FieldAccess(Id(a),Id($a)),IntLit(1)),AssignStmt(ArrayCell(Id(a),[Id(a)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])])]),ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])]),IntLit(1)),AssignStmt(ArrayCell(FieldAccess(FieldAccess(FieldAccess(Id(class),Id($a)),Id(a)),Id(a)),[ArrayCell(FieldAccess(Id(class),Id($a)),[IntLit(1)]),ArrayCell(FieldAccess(Id(class),Id(a)),[IntLit(1)])]),IntLit(1)),AssignStmt(FieldAccess(Self(),Id(a)),IntLit(1)),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Self(),Id(a)),Id(a)),Id(a)),IntLit(1))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,359))
    
    def test_360_a_lot_op(self):
        str_in = """
Class Program{
    main () {
        foo = New foo();
        foo = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo[a] = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo[a[a]] = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo[a][a][a][a] = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo.foo = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo.foo.foo.z = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo::$foo = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
        foo::$foo().foo.z = a && a || b * c + d / e - f % (z + z.z / c::$z - c::$z());
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(foo),NewExpr(Id(foo),[])),AssignStmt(Id(foo),BinaryOp(||,BinaryOp(&&,Id(a),Id(a)),BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(b),Id(c)),BinaryOp(/,Id(d),Id(e))),BinaryOp(%,Id(f),BinaryOp(-,BinaryOp(+,Id(z),BinaryOp(/,FieldAccess(Id(z),Id(z)),FieldAccess(Id(c),Id($z)))),CallExpr(Id(c),Id($z),[])))))),AssignStmt(ArrayCell(Id(foo),[Id(a)]),BinaryOp(||,BinaryOp(&&,Id(a),Id(a)),BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(b),Id(c)),BinaryOp(/,Id(d),Id(e))),BinaryOp(%,Id(f),BinaryOp(-,BinaryOp(+,Id(z),BinaryOp(/,FieldAccess(Id(z),Id(z)),FieldAccess(Id(c),Id($z)))),CallExpr(Id(c),Id($z),[])))))),AssignStmt(ArrayCell(Id(foo),[ArrayCell(Id(a),[Id(a)])]),BinaryOp(||,BinaryOp(&&,Id(a),Id(a)),BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(b),Id(c)),BinaryOp(/,Id(d),Id(e))),BinaryOp(%,Id(f),BinaryOp(-,BinaryOp(+,Id(z),BinaryOp(/,FieldAccess(Id(z),Id(z)),FieldAccess(Id(c),Id($z)))),CallExpr(Id(c),Id($z),[])))))),AssignStmt(ArrayCell(Id(foo),[Id(a),Id(a),Id(a),Id(a)]),BinaryOp(||,BinaryOp(&&,Id(a),Id(a)),BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(b),Id(c)),BinaryOp(/,Id(d),Id(e))),BinaryOp(%,Id(f),BinaryOp(-,BinaryOp(+,Id(z),BinaryOp(/,FieldAccess(Id(z),Id(z)),FieldAccess(Id(c),Id($z)))),CallExpr(Id(c),Id($z),[])))))),AssignStmt(FieldAccess(Id(foo),Id(foo)),BinaryOp(||,BinaryOp(&&,Id(a),Id(a)),BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(b),Id(c)),BinaryOp(/,Id(d),Id(e))),BinaryOp(%,Id(f),BinaryOp(-,BinaryOp(+,Id(z),BinaryOp(/,FieldAccess(Id(z),Id(z)),FieldAccess(Id(c),Id($z)))),CallExpr(Id(c),Id($z),[])))))),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(foo),Id(foo)),Id(foo)),Id(z)),BinaryOp(||,BinaryOp(&&,Id(a),Id(a)),BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(b),Id(c)),BinaryOp(/,Id(d),Id(e))),BinaryOp(%,Id(f),BinaryOp(-,BinaryOp(+,Id(z),BinaryOp(/,FieldAccess(Id(z),Id(z)),FieldAccess(Id(c),Id($z)))),CallExpr(Id(c),Id($z),[])))))),AssignStmt(FieldAccess(Id(foo),Id($foo)),BinaryOp(||,BinaryOp(&&,Id(a),Id(a)),BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(b),Id(c)),BinaryOp(/,Id(d),Id(e))),BinaryOp(%,Id(f),BinaryOp(-,BinaryOp(+,Id(z),BinaryOp(/,FieldAccess(Id(z),Id(z)),FieldAccess(Id(c),Id($z)))),CallExpr(Id(c),Id($z),[])))))),AssignStmt(FieldAccess(FieldAccess(CallExpr(Id(foo),Id($foo),[]),Id(foo)),Id(z)),BinaryOp(||,BinaryOp(&&,Id(a),Id(a)),BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(b),Id(c)),BinaryOp(/,Id(d),Id(e))),BinaryOp(%,Id(f),BinaryOp(-,BinaryOp(+,Id(z),BinaryOp(/,FieldAccess(Id(z),Id(z)),FieldAccess(Id(c),Id($z)))),CallExpr(Id(c),Id($z),[]))))))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,360))

    def test_361_if_statement(self):
        str_in = """
Class Program{
    main () {
        If (2>1) {
            Var a,b,c: Int;
            If (a-b-c == 100) {
                a = b;
                b = c;
                c = a;
            }
            Elseif (a+b+c >= 200) {
                a = b;
                b = c;
                c = a;
            }
            Elseif (a+b+c >= 200) {}
            Elseif (a+b+c >= 200) {}
            Else {
                a = b - c;
            }
        }
        Elseif (a+b+c >= 200) {
            Var a,b,c: Int;
            If (a-b-c == 100) {
                a = b;
                b = c;
                c = a;
            }
            Elseif (a+b+c >= 200) {
                a = b;
                b = c;
                c = a;
            }
            Elseif (a+b+c >= 200) {}
            Elseif (a+b+c >= 200) {}
            Else {
                a = b - c;
            }
        }
        Elseif (a+b+c >= 200) {
            Var a,b,c: Int;
            If (a-b-c == 100) {
                a = b;
                b = c;
                c = a;
            }
            Elseif (a+b+c >= 200) {
                a = b;
                b = c;
                c = a;
            }
            Elseif (a+b+c >= 200) {}
            Elseif (a+b+c >= 200) {}
            Else {
                a = b - c;
            }
        }
        Else {
            c = 3;
        }
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>,IntLit(2),IntLit(1)),Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(c)),AssignStmt(Id(c),Id(a))]),If(BinaryOp(>=,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLit(200)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(c)),AssignStmt(Id(c),Id(a))]),If(BinaryOp(>=,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLit(200)),Block([]),If(BinaryOp(>=,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLit(200)),Block([]),Block([AssignStmt(Id(a),BinaryOp(-,Id(b),Id(c)))])))))]),If(BinaryOp(>=,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLit(200)),Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(c)),AssignStmt(Id(c),Id(a))]),If(BinaryOp(>=,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLit(200)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(c)),AssignStmt(Id(c),Id(a))]),If(BinaryOp(>=,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLit(200)),Block([]),If(BinaryOp(>=,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLit(200)),Block([]),Block([AssignStmt(Id(a),BinaryOp(-,Id(b),Id(c)))])))))]),If(BinaryOp(>=,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLit(200)),Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(c)),AssignStmt(Id(c),Id(a))]),If(BinaryOp(>=,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLit(200)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(c)),AssignStmt(Id(c),Id(a))]),If(BinaryOp(>=,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLit(200)),Block([]),If(BinaryOp(>=,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLit(200)),Block([]),Block([AssignStmt(Id(a),BinaryOp(-,Id(b),Id(c)))])))))]),Block([AssignStmt(Id(c),IntLit(3))]))))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,361))
    
    def test_362_simple_if(self):
        str_in = """
Class Program {
    main() {
        If (a-b-c == 100) {
            a = b;
            b = c;
            c = d;
        }
        Else {
            a = b - c;
        }
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(c)),AssignStmt(Id(c),Id(d))]),Block([AssignStmt(Id(a),BinaryOp(-,Id(b),Id(c)))]))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,362))
    
    def test_363_sign_expr(self):
        str_in = """
Class Program {
    main () {
        a = -10;
        a = !10;
        a = -10 - 10;
        a = !10 + 10;
        a = -10 - 10 + 10 --1;
        a = -10 - !10;
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),UnaryOp(-,IntLit(10))),AssignStmt(Id(a),UnaryOp(!,IntLit(10))),AssignStmt(Id(a),BinaryOp(-,UnaryOp(-,IntLit(10)),IntLit(10))),AssignStmt(Id(a),BinaryOp(+,UnaryOp(!,IntLit(10)),IntLit(10))),AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,BinaryOp(-,UnaryOp(-,IntLit(10)),IntLit(10)),IntLit(10)),UnaryOp(-,IntLit(1)))),AssignStmt(Id(a),BinaryOp(-,UnaryOp(-,IntLit(10)),UnaryOp(!,IntLit(10))))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,363))
    
    def test_364_left_hand_side(self):
        str_in = """
Class Program{
    main () {
        a::$a = "foo" || "foo" && "foo" * 0 / 0x0 % (a  + a.a + class::$a- a.a() - class::$a());
        a::$a.a = "foo" || "foo" && "foo" * 0 / 0x0 % (a  + a.a + class::$a- a.a() - class::$a());
        a[1][1][1] = "foo" || "foo" && "foo" * 0 / 0x0 % (a + a.a + class::$a- a.a() - class::$a());
        a[a[a[a[1]]]][a[a[a]]] = "foo" || "foo" && "foo" * 0 / 0x0 % (a + a.a + class::$a- a.a() - class::$a());
        a.a = "foo" || "foo" && "foo" * 0 / 0x0 % (a  + a.a + class::$a - a.a() - class::$a());
        a.a.a = "foo" || "foo" && "foo" * 0 / 0x0 % (a  + a.a + class::$a- a.a() - class::$a());
        a = "foo" || "foo" && "foo" * 0 / 0x0 % (a + a.a + class::$a - a.a() - class::$a());
        a[1] = "foo" || "foo" && "foo" * 0 / 0x0 % (a + a.a + class::$a- a.a() - class::$a());
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(a),Id($a)),BinaryOp(&&,BinaryOp(||,StringLit(foo),StringLit(foo)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(foo),IntLit(0)),IntLit(0)),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(class),Id($a))),CallExpr(Id(a),Id(a),[])),CallExpr(Id(class),Id($a),[]))))),AssignStmt(FieldAccess(FieldAccess(Id(a),Id($a)),Id(a)),BinaryOp(&&,BinaryOp(||,StringLit(foo),StringLit(foo)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(foo),IntLit(0)),IntLit(0)),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(class),Id($a))),CallExpr(Id(a),Id(a),[])),CallExpr(Id(class),Id($a),[]))))),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1),IntLit(1)]),BinaryOp(&&,BinaryOp(||,StringLit(foo),StringLit(foo)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(foo),IntLit(0)),IntLit(0)),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(class),Id($a))),CallExpr(Id(a),Id(a),[])),CallExpr(Id(class),Id($a),[]))))),AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])]),ArrayCell(Id(a),[ArrayCell(Id(a),[Id(a)])])]),BinaryOp(&&,BinaryOp(||,StringLit(foo),StringLit(foo)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(foo),IntLit(0)),IntLit(0)),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(class),Id($a))),CallExpr(Id(a),Id(a),[])),CallExpr(Id(class),Id($a),[]))))),AssignStmt(FieldAccess(Id(a),Id(a)),BinaryOp(&&,BinaryOp(||,StringLit(foo),StringLit(foo)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(foo),IntLit(0)),IntLit(0)),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(class),Id($a))),CallExpr(Id(a),Id(a),[])),CallExpr(Id(class),Id($a),[]))))),AssignStmt(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),BinaryOp(&&,BinaryOp(||,StringLit(foo),StringLit(foo)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(foo),IntLit(0)),IntLit(0)),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(class),Id($a))),CallExpr(Id(a),Id(a),[])),CallExpr(Id(class),Id($a),[]))))),AssignStmt(Id(a),BinaryOp(&&,BinaryOp(||,StringLit(foo),StringLit(foo)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(foo),IntLit(0)),IntLit(0)),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(class),Id($a))),CallExpr(Id(a),Id(a),[])),CallExpr(Id(class),Id($a),[]))))),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),BinaryOp(&&,BinaryOp(||,StringLit(foo),StringLit(foo)),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(foo),IntLit(0)),IntLit(0)),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),FieldAccess(Id(a),Id(a))),FieldAccess(Id(class),Id($a))),CallExpr(Id(a),Id(a),[])),CallExpr(Id(class),Id($a),[])))))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,364))
    
    def test_365_if_with_missing_part(self):
        str_in = """
Class Program {
    main() {
        If (a-b-c == 100) {
            If (a-b-c == 100) {
                a = b;
                c = d;
            }
            If (a-b-c == 100) {
                a = b;
                c = d;
            }
        }
        Else {
            If (a-b-c == 100) {
                a = b;
                c = d;
            }
        }
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(c),Id(d))])),If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(c),Id(d))]))]),Block([If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(c),Id(d))]))]))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,365))
    
    def test__366_simple_program_double(self):
        str_in = """Class Program {}
                    Class Foo {}"""
        expect = """Program([ClassDecl(Id(Program),[]),ClassDecl(Id(Foo),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,366))

    def test_367_for_each(self):
        str_in = """
Class Program {
    main () {
        Foreach(i In 1 .. 100 By z) {
            If (True || True) {
                x = y;
            }
            Elseif (True && True) {
                y = z;
            }
        }
        Foreach(i In 1 .. 100 By z) {
            Foreach(j In 1 .. 100 By z) {
                Foreach(k In 1 .. 100 By z) {
                    a = b + c;
                }
            }
        }
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(1),IntLit(100),Id(z),Block([If(BinaryOp(||,BooleanLit(True),BooleanLit(True)),Block([AssignStmt(Id(x),Id(y))]),If(BinaryOp(&&,BooleanLit(True),BooleanLit(True)),Block([AssignStmt(Id(y),Id(z))])))])]),For(Id(i),IntLit(1),IntLit(100),Id(z),Block([For(Id(j),IntLit(1),IntLit(100),Id(z),Block([For(Id(k),IntLit(1),IntLit(100),Id(z),Block([AssignStmt(Id(a),BinaryOp(+,Id(b),Id(c)))])])])])])])]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,367))
    
    def test_368_sign_expr(self):
        str_in = """
Class Program {
    main () {
        a = !!!!!!!!!!!!1;
        a = ------------1;
        a = ------------1 - !!!!!!!!!!!1 + 1;
        a = ------------1 || !!!!!!!!!!!1 && 1;
        a = ------------(2*3+4);
        a = !!!!!!!!!!!!(2*3+4);
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,IntLit(1)))))))))))))),AssignStmt(Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1)))))))))))))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1))))))))))))),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,IntLit(1))))))))))))),IntLit(1))),AssignStmt(Id(a),BinaryOp(&&,BinaryOp(||,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1))))))))))))),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,IntLit(1))))))))))))),IntLit(1))),AssignStmt(Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,BinaryOp(+,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(4))))))))))))))),AssignStmt(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,BinaryOp(+,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(4)))))))))))))))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,368))
    
    def test_369_for_each_stmt(self):
        str_in = """
Class Program {
    main () {
        Foreach(i In 1+2-3 .. 100) {
            If (True || True) {
                x = y;
            }
            Elseif (True && True) {
                y = z;
            }
        }
        Foreach(i In x+yield .. 100 By z) {
            Foreach(j In a+b-c*d .. 25 &&y) {
                Foreach(k In 1 .. 100) {
                    a = b + c;
                }
            }
        }
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(100),IntLit(1),Block([If(BinaryOp(||,BooleanLit(True),BooleanLit(True)),Block([AssignStmt(Id(x),Id(y))]),If(BinaryOp(&&,BooleanLit(True),BooleanLit(True)),Block([AssignStmt(Id(y),Id(z))])))])]),For(Id(i),BinaryOp(+,Id(x),Id(yield)),IntLit(100),Id(z),Block([For(Id(j),BinaryOp(-,BinaryOp(+,Id(a),Id(b)),BinaryOp(*,Id(c),Id(d))),BinaryOp(&&,IntLit(25),Id(y)),IntLit(1),Block([For(Id(k),IntLit(1),IntLit(100),IntLit(1),Block([AssignStmt(Id(a),BinaryOp(+,Id(b),Id(c)))])])])])])])]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,369))
    
    def test_370_index_expr(self):
        str_in = """
Class Program {
    main() {
        a = a[1];
        a = a[1][1][1][1][1];
        a = a[a[a[1]]][a[a[a[1]]]];
        a = class::$method(a, b, c)[1][1][1];
        a = class.class.class[1][1][1][a[a[1]]];
        a = a[a.a[1]][a.a.a.a.a[1]];
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(1)])),AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(1),IntLit(1),IntLit(1),IntLit(1),IntLit(1)])),AssignStmt(Id(a),ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])]),ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])])])),AssignStmt(Id(a),ArrayCell(CallExpr(Id(class),Id($method),[Id(a),Id(b),Id(c)]),[IntLit(1),IntLit(1),IntLit(1)])),AssignStmt(Id(a),ArrayCell(FieldAccess(FieldAccess(Id(class),Id(class)),Id(class)),[IntLit(1),IntLit(1),IntLit(1),ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])])),AssignStmt(Id(a),ArrayCell(Id(a),[ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1)]),ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),Id(a)),Id(a)),[IntLit(1)])]))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,370))
    
    def test_371_for_each_with_static(self):
        str_in = """
Class Program {
    main() {
        Foreach(i In class::$var .. 100) {}
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),FieldAccess(Id(class),Id($var)),IntLit(100),IntLit(1),Block([])])]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,371))
    
    def test_372_index_expr(self):
        str_in = """
Class the_class {
    Val $int1: Array[Int, 1] = a[1];
    Val $int2: Array[Array[Int, 1], 1] = a[1][2];
    Val $a: Array[Array[Array[Int, 1],1], 1] = a[1][2][3];
    Var $b: Int =  a[1][2][3][4];
    Var $c: Int =  a[a[a[1]]];
                    
    Constructor(a: Int; b: Float) {
        str1 = a[1];
        Val str2: Array[Array[Int, 1], 1] = a[1][2];
        Val a: Array[Array[Array[Int, 1],1], 1] = a[1][2][3];
        c =  a[1][2][3][4];
        d =  a[a[a[1]]];
    }
    Destructor() {}
}        
        """
        expect = """Program([ClassDecl(Id(the_class),[AttributeDecl(Static,ConstDecl(Id($int1),ArrayType(1,IntType),ArrayCell(Id(a),[IntLit(1)]))),AttributeDecl(Static,ConstDecl(Id($int2),ArrayType(1,ArrayType(1,IntType)),ArrayCell(Id(a),[IntLit(1),IntLit(2)]))),AttributeDecl(Static,ConstDecl(Id($a),ArrayType(1,ArrayType(1,ArrayType(1,IntType))),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]))),AttributeDecl(Static,VarDecl(Id($b),IntType,ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]))),AttributeDecl(Static,VarDecl(Id($c),IntType,ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])]))),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([AssignStmt(Id(str1),ArrayCell(Id(a),[IntLit(1)])),ConstDecl(Id(str2),ArrayType(1,ArrayType(1,IntType)),ArrayCell(Id(a),[IntLit(1),IntLit(2)])),ConstDecl(Id(a),ArrayType(1,ArrayType(1,ArrayType(1,IntType))),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)])),AssignStmt(Id(c),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])),AssignStmt(Id(d),ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])]))])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,372))
    
    def test_373_simple_program_8(self):
        str_in = """
Class Program {
    main() {
        Break;
        Continue;
        Return a.foo();
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Break,Continue,Return(CallExpr(Id(a),Id(foo),[]))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,373))
    
    def test_374_return_nothing(self):
        str_in = """
Class Program{
    main () {
        Return;
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return()]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,374))
    
    def test_375_simple_program_6(self):
        str_in = """Class Program {
            $Main(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($Main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,375))
    
    def test__376_continue_and_if(self):
        str_in = """
Class Program{
    main () {
        If (a-b-c == 100) {
            If (a-b-c == 100) {
                a = b;
                c = d;
            }
            If (a-b-c == 100) {
                Continue;
                c = d;
            }
        }
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(c),Id(d))])),If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([Continue,AssignStmt(Id(c),Id(d))]))]))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,376))

    def test_377_simple_program_double_2(self):
        str_in = """Class Program : Computer {}
                    Class Foo : TheFoo {}"""
        expect = """Program([ClassDecl(Id(Program),Id(Computer),[]),ClassDecl(Id(Foo),Id(TheFoo),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,377))
    
    def test_378_method_stmt(self):
        str_in = """
Class Program{
    method_a (a: Float) {
        If (a-b-c == 100) {
            a = b;
            c = d;
        }
    }
    $method_b (a: Float) {
        If (a-b-c == 100) {
            a = b;
            c = d;
        }
    }
    Constructor(a: Float) {}
    Destructor(){}
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method_a),Instance,[param(Id(a),FloatType)],Block([If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(c),Id(d))]))])),MethodDecl(Id($method_b),Static,[param(Id(a),FloatType)],Block([If(BinaryOp(==,BinaryOp(-,BinaryOp(-,Id(a),Id(b)),Id(c)),IntLit(100)),Block([AssignStmt(Id(a),Id(b)),AssignStmt(Id(c),Id(d))]))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),FloatType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,378))
    
    def test_379_simple_program_double_4(self):
        str_in = """Class Program {
            Destructor(){}
            Constructor(){}
            Destructor(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,379))
    
    def test_380_method_stmt(self):
        str_in = """
Class Program {
    main () {
        class.method(a,b,c);
        class.method(1+2+3+4+5);
        class::$assertTrue(NotImplemented);
        class.a.b.c.d.e.f.g.h.i.k.l.m();
        class::$assertTrue.assertTrue.abc.d.e();
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(class),Id(method),[Id(a),Id(b),Id(c)]),Call(Id(class),Id(method),[BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5))]),Call(Id(class),Id($assertTrue),[Id(NotImplemented)]),Call(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(class),Id(a)),Id(b)),Id(c)),Id(d)),Id(e)),Id(f)),Id(g)),Id(h)),Id(i)),Id(k)),Id(l)),Id(m),[]),Call(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(class),Id($assertTrue)),Id(assertTrue)),Id(abc)),Id(d)),Id(e),[])]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,380))

    def test_381_simple_program_2(self):
        str_in = """Class Program : Computer {}"""
        expect = """Program([ClassDecl(Id(Program),Id(Computer),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,381))
    
    def test_382_self(self):
        str_in = """
Class Program{
    main () {
        Self.a = 3;
        Self.b.c.d.e.f.g.h.i.k.l.m();
        Self.Method(a,b,c,d,e,f,g);
    }
    
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(3)),Call(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Self(),Id(b)),Id(c)),Id(d)),Id(e)),Id(f)),Id(g)),Id(h)),Id(i)),Id(k)),Id(l)),Id(m),[]),Call(Self(),Id(Method),[Id(a),Id(b),Id(c),Id(d),Id(e),Id(f),Id(g)])]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,382))
    
    def test_383_simple_program_4(self):
        str_in = """Class Program {
            Destructor(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,383))
    
    def test_384_self_in_methods(self):
        str_in = """
Class Program{
    Val $susan, agent: Int = 0, 175;
    $Method() {
        a.Method(Self.b.Method(Self.a.Method()));
    }
    main () {
        Foreach (a In 1 .. Self.a().Value.c.d.e.foo_method) {
            Self.a().Method();
        }
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($susan),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(agent),IntType,IntLit(175))),MethodDecl(Id($Method),Static,[],Block([Call(Id(a),Id(Method),[CallExpr(FieldAccess(Self(),Id(b)),Id(Method),[CallExpr(FieldAccess(Self(),Id(a)),Id(Method),[])])])])),MethodDecl(Id(main),Static,[],Block([For(Id(a),IntLit(1),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(CallExpr(Self(),Id(a),[]),Id(Value)),Id(c)),Id(d)),Id(e)),Id(foo_method)),IntLit(1),Block([Call(CallExpr(Self(),Id(a),[]),Id(Method),[])])])]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,384))
    
    def test_385_simple_program_6(self):
        str_in = """Class Program {
            $Main(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($Main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,385))
    
    def test__386_statememt_mash_up(self):
        str_in = """
## Say hi to papa USA ##
Class NorthKorea {
    Var $num_of_nuclear_nuke: Int = 999;
    Val $leader: String = "kim jong un";
    $Scare_little_dick_Southern_chicks(solders, cannons: Int) {
        Self.show_off_at_borders(solders, cannons);
    } 
}

Class SouthKorea{
    main () {
        Foreach (year In 1953 .. now By 1) {
            If (NorthKorea.test_nuke() == True) {
                Self.call_papa_USA();
                Break;
            }
            Elseif (NorthKorea.prepare_to_test_nuke == True) {
                Self.call_papa_USA();
            }
            Else {
                Self.pay_money_for_papa_USA();
                Continue;
            }
            USA.good_kiz = SouthKorea;
            Return USA.good_kiz;
        }
    }
}        
        """
        expect = """Program([ClassDecl(Id(NorthKorea),[AttributeDecl(Static,VarDecl(Id($num_of_nuclear_nuke),IntType,IntLit(999))),AttributeDecl(Static,ConstDecl(Id($leader),StringType,StringLit(kim jong un))),MethodDecl(Id($Scare_little_dick_Southern_chicks),Static,[param(Id(solders),IntType),param(Id(cannons),IntType)],Block([Call(Self(),Id(show_off_at_borders),[Id(solders),Id(cannons)])]))]),ClassDecl(Id(SouthKorea),[MethodDecl(Id(main),Instance,[],Block([For(Id(year),IntLit(1953),Id(now),IntLit(1),Block([If(BinaryOp(==,CallExpr(Id(NorthKorea),Id(test_nuke),[]),BooleanLit(True)),Block([Call(Self(),Id(call_papa_USA),[]),Break]),If(BinaryOp(==,FieldAccess(Id(NorthKorea),Id(prepare_to_test_nuke)),BooleanLit(True)),Block([Call(Self(),Id(call_papa_USA),[])]),Block([Call(Self(),Id(pay_money_for_papa_USA),[]),Continue]))),AssignStmt(FieldAccess(Id(USA),Id(good_kiz)),Id(SouthKorea)),Return(FieldAccess(Id(USA),Id(good_kiz)))])])]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,386))

    def test_387_simple_program_double_2(self):
        str_in = """Class Program : Computer {}
                    Class Foo : TheFoo {}"""
        expect = """Program([ClassDecl(Id(Program),Id(Computer),[]),ClassDecl(Id(Foo),Id(TheFoo),[])])"""
        self.assertTrue(TestAST.test(str_in,expect,387))
    
    def test_388_complex_program_w_all_stmt(self):
        str_in = """
Class Foo : Foo_2 {
    Var a, $a: Array[Array[Array[String, 3],3],3];
    Val a: Array[Array[Array[String, 3],3],3] = Array(Array(Array(Array(Array(Array(Array(Array(Array(Array(Array(3,4,5)))))))))));

    foo_method(a,b,c: String; d,e,f: Float; g,h,i: Array[Array[Array[Boolean, 2], 2], 2]) {
        Var a, b: Array[Array[Array[String, 3],3],3];
        Val a: Array[Array[Array[String, 3],3],3] = Array(Array(Array(Array(Array(Array(Array(Array(Array(Array(Array(3,4,5)))))))))));

        If (a >= Nulll) {
            foo.do_something();
        }
        Elseif (Self.objects) {
            Continue;
        }
        Else {
            Foreach (i In class::$a .. class::$b() By class.d()) {
                If (a >= Nulll) {
                    foo.do_something();
                }
                Elseif (Self.objects) {
                    Continue;
                }
                Else {
                    Break;
                }
            }
        }
        Return Self.objects;
    }
    Constructor(a,b,c: String){
        a.do_something();
    }
    Destructor(){}
}
Class Program { 
    main () {}
}        
        """
        expect = """Program([ClassDecl(Id(Foo),Id(Foo_2),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(3,ArrayType(3,ArrayType(3,StringType))))),AttributeDecl(Static,VarDecl(Id($a),ArrayType(3,ArrayType(3,ArrayType(3,StringType))))),AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(3,ArrayType(3,ArrayType(3,StringType))),[[[[[[[[[[[IntLit(3),IntLit(4),IntLit(5)]]]]]]]]]]])),MethodDecl(Id(foo_method),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),StringType),param(Id(d),FloatType),param(Id(e),FloatType),param(Id(f),FloatType),param(Id(g),ArrayType(2,ArrayType(2,ArrayType(2,BoolType)))),param(Id(h),ArrayType(2,ArrayType(2,ArrayType(2,BoolType)))),param(Id(i),ArrayType(2,ArrayType(2,ArrayType(2,BoolType))))],Block([VarDecl(Id(a),ArrayType(3,ArrayType(3,ArrayType(3,StringType)))),VarDecl(Id(b),ArrayType(3,ArrayType(3,ArrayType(3,StringType)))),ConstDecl(Id(a),ArrayType(3,ArrayType(3,ArrayType(3,StringType))),[[[[[[[[[[[IntLit(3),IntLit(4),IntLit(5)]]]]]]]]]]]),If(BinaryOp(>=,Id(a),Id(Nulll)),Block([Call(Id(foo),Id(do_something),[])]),If(FieldAccess(Self(),Id(objects)),Block([Continue]),Block([For(Id(i),FieldAccess(Id(class),Id($a)),CallExpr(Id(class),Id($b),[]),CallExpr(Id(class),Id(d),[]),Block([If(BinaryOp(>=,Id(a),Id(Nulll)),Block([Call(Id(foo),Id(do_something),[])]),If(FieldAccess(Self(),Id(objects)),Block([Continue]),Block([Break])))])])]))),Return(FieldAccess(Self(),Id(objects)))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),StringType)],Block([Call(Id(a),Id(do_something),[])])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,388))
    
    def test_389_simple_program_double_4(self):
        str_in = """Class Program {
            Destructor(){}
            Constructor(){}
            Destructor(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,389))
    
    def test_390_mix_class(self):
        str_in = """
Class Keyboard {
    Var pcb: PCB;
    Var case: Material;
    Typing() {
        Self.send_signal_when_press_a_button();
    }
}

Class Mechanical_keyboard : Keyboard {
    Var switches: String;
    Var led_rgb: Boolean;
    Sound(buttons, case, switches, pcb: Part_of_keyboard) {
        Return Self.sound;
    }
}

Class Program {
    main () {
        Self.sound_test(Mechanical_keyboard);
    }
}        
        """
        expect = """Program([ClassDecl(Id(Keyboard),[AttributeDecl(Instance,VarDecl(Id(pcb),ClassType(Id(PCB)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(case),ClassType(Id(Material)),NullLiteral())),MethodDecl(Id(Typing),Instance,[],Block([Call(Self(),Id(send_signal_when_press_a_button),[])]))]),ClassDecl(Id(Mechanical_keyboard),Id(Keyboard),[AttributeDecl(Instance,VarDecl(Id(switches),StringType)),AttributeDecl(Instance,VarDecl(Id(led_rgb),BoolType)),MethodDecl(Id(Sound),Instance,[param(Id(buttons),ClassType(Id(Part_of_keyboard))),param(Id(case),ClassType(Id(Part_of_keyboard))),param(Id(switches),ClassType(Id(Part_of_keyboard))),param(Id(pcb),ClassType(Id(Part_of_keyboard)))],Block([Return(FieldAccess(Self(),Id(sound)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Self(),Id(sound_test),[Id(Mechanical_keyboard)])]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,390))
    
    def test_391_simple_program_double_6(self):
        str_in = """Class Program {
            $Main(){}
            $Foo(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($Main),Static,[],Block([])),MethodDecl(Id($Foo),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,391))
    
    def test_392_new(self):
        str_in = """
Class Program {
    main () {
        a = New foo(index);
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(foo),[Id(index)]))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,392))
    
    def test_393_mem_access(self):
        str_in = """
Class Program {
    main () {
        a = class.a;
        a = class.a.a;
        a = class.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a;

        a = class::$a;
        a = class::$a.a;
        a = class::$a.a.a.a.a;

        a = class.method();
        a = class.method().method();
        a = class.method().method().method().method().method();

        a = class.method().a;
        a = class.method().a.method();
        a = class.method().method().a.a.a.method().method();

        a = class::$a;
        a = class::$a.a();
        a = class::$a().a.a.a().a;

        a = (12345).a;
        a = (0).a();
        a = ("foo").a();
        
        a = New foo().a.c.d;
        a = New bar().a.c().d();
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),FieldAccess(Id(class),Id(a))),AssignStmt(Id(a),FieldAccess(FieldAccess(Id(class),Id(a)),Id(a))),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(class),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a))),AssignStmt(Id(a),FieldAccess(Id(class),Id($a))),AssignStmt(Id(a),FieldAccess(FieldAccess(Id(class),Id($a)),Id(a))),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(class),Id($a)),Id(a)),Id(a)),Id(a)),Id(a))),AssignStmt(Id(a),CallExpr(Id(class),Id(method),[])),AssignStmt(Id(a),CallExpr(CallExpr(Id(class),Id(method),[]),Id(method),[])),AssignStmt(Id(a),CallExpr(CallExpr(CallExpr(CallExpr(CallExpr(Id(class),Id(method),[]),Id(method),[]),Id(method),[]),Id(method),[]),Id(method),[])),AssignStmt(Id(a),FieldAccess(CallExpr(Id(class),Id(method),[]),Id(a))),AssignStmt(Id(a),CallExpr(FieldAccess(CallExpr(Id(class),Id(method),[]),Id(a)),Id(method),[])),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(FieldAccess(FieldAccess(CallExpr(CallExpr(Id(class),Id(method),[]),Id(method),[]),Id(a)),Id(a)),Id(a)),Id(method),[]),Id(method),[])),AssignStmt(Id(a),FieldAccess(Id(class),Id($a))),AssignStmt(Id(a),CallExpr(FieldAccess(Id(class),Id($a)),Id(a),[])),AssignStmt(Id(a),FieldAccess(CallExpr(FieldAccess(FieldAccess(CallExpr(Id(class),Id($a),[]),Id(a)),Id(a)),Id(a),[]),Id(a))),AssignStmt(Id(a),FieldAccess(IntLit(12345),Id(a))),AssignStmt(Id(a),CallExpr(IntLit(0),Id(a),[])),AssignStmt(Id(a),CallExpr(StringLit(foo),Id(a),[])),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(foo),[]),Id(a)),Id(c)),Id(d))),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(NewExpr(Id(bar),[]),Id(a)),Id(c),[]),Id(d),[]))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,393))
    
    def test_394_string_expr(self):
        str_in = """
Class Program{
    main () {
        Var a : String = "empty string";
        a = "a-c+d" + "abcde";
        a = "a-c+d" - "abcde";
        a = "a-c+d" * "abcde" / "a-c+d" % "abcde";
        a = "a-c+d" +. "abcde";
        a = "a-c+d" != "abcde";
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),StringType,StringLit(empty string)),AssignStmt(Id(a),BinaryOp(+,StringLit(a-c+d),StringLit(abcde))),AssignStmt(Id(a),BinaryOp(-,StringLit(a-c+d),StringLit(abcde))),AssignStmt(Id(a),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLit(a-c+d),StringLit(abcde)),StringLit(a-c+d)),StringLit(abcde))),AssignStmt(Id(a),BinaryOp(+.,StringLit(a-c+d),StringLit(abcde))),AssignStmt(Id(a),BinaryOp(!=,StringLit(a-c+d),StringLit(abcde)))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,394))
    
    def test_395_simple_program_6(self):
        str_in = """Class Program {
            $Main(){}
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($Main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,395))
    
    def test__396_simple_program_double(self):
        str_in = """
Class Program {
    main () {
        a = 1||2||3||4||5||6;
        a = 1&&2&&3&&4&&5&&6; 
        a = 1+2+3+4+5+6;
        a = 1-2-3-4-5-6;
        a = 1*2*3*4*5*6;
        a = 1/ 2/3/4/5/6;
        a = 1% 2 % 3 %  4 % 5 % 6;
        a = !!!!!!!!1;
        a = --------1;
        a = b[1][1][1][1+2+3][variable];
        a = b[b[b[b[1]]]];
        a = a.b.c.d.e.f;
        a = a.b.c.method().method().a.b.method().method();
        a = a::$b().method().a.method().a.method();
        a = New a(New a(New a()));
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(||,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),BinaryOp(&&,BinaryOp(&&,BinaryOp(&&,BinaryOp(&&,BinaryOp(&&,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),BinaryOp(-,BinaryOp(-,BinaryOp(-,BinaryOp(-,BinaryOp(-,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),BinaryOp(*,BinaryOp(*,BinaryOp(*,BinaryOp(*,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),BinaryOp(/,BinaryOp(/,BinaryOp(/,BinaryOp(/,BinaryOp(/,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),BinaryOp(%,BinaryOp(%,BinaryOp(%,BinaryOp(%,BinaryOp(%,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))),AssignStmt(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,IntLit(1)))))))))),AssignStmt(Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1)))))))))),AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(1),IntLit(1),IntLit(1),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),Id(variable)])),AssignStmt(Id(a),ArrayCell(Id(b),[ArrayCell(Id(b),[ArrayCell(Id(b),[ArrayCell(Id(b),[IntLit(1)])])])])),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)),Id(e)),Id(f))),AssignStmt(Id(a),CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(method),[]),Id(method),[]),Id(a)),Id(b)),Id(method),[]),Id(method),[])),AssignStmt(Id(a),CallExpr(FieldAccess(CallExpr(FieldAccess(CallExpr(CallExpr(Id(a),Id($b),[]),Id(method),[]),Id(a)),Id(method),[]),Id(a)),Id(method),[])),AssignStmt(Id(a),NewExpr(Id(a),[NewExpr(Id(a),[NewExpr(Id(a),[])])]))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,396))

    def test_397_alot_operator(self):
        str_in = """
Class Program{
    main () {
        a= New a(New a(New a((a[a[a[a[a[1]]]]][a]).method()+ !!!!----1/2*3%4+5)));
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(a),[NewExpr(Id(a),[NewExpr(Id(a),[BinaryOp(+,BinaryOp(+,CallExpr(ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])])]),Id(a)]),Id(method),[]),BinaryOp(%,BinaryOp(*,BinaryOp(/,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(1))))))))),IntLit(2)),IntLit(3)),IntLit(4))),IntLit(5))])])]))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,397))
    
    def test_398_relation_expr(self):
        str_in = """
Class Program{
    main () {
        a = a == 1;
        a = 1 < 2;
        a = 1 <= 2;
        a = a > 3;
        a = a >= 3;
        a = a != 4;
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(==,Id(a),IntLit(1))),AssignStmt(Id(a),BinaryOp(<,IntLit(1),IntLit(2))),AssignStmt(Id(a),BinaryOp(<=,IntLit(1),IntLit(2))),AssignStmt(Id(a),BinaryOp(>,Id(a),IntLit(3))),AssignStmt(Id(a),BinaryOp(>=,Id(a),IntLit(3))),AssignStmt(Id(a),BinaryOp(!=,Id(a),IntLit(4)))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,398))
    
    def test_399_logical_expr(self):
        str_in = """
Class Program{
    main () {
        a = a && b;
        a = c || d;
    }
}        
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(&&,Id(a),Id(b))),AssignStmt(Id(a),BinaryOp(||,Id(c),Id(d)))]))])])"""
        self.assertTrue(TestAST.test(str_in,expect,399))
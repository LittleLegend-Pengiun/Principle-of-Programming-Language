import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_000_redeclare_variable(self):
        input = """
            Class A {
                Var x, y: Int = 1, 1;
                method(a,b: Int) {
                    Var x, y : Int = Self.x, Self.y;
                    Var x: Int = x;
                }
            }
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_001_redeclare_variable_with_parameter(self):
        input = """
            Class A {
                Var x, y: Int = 1, 1;
                method(a,b: Int) {
                    Var x, y : Int = Self.x, Self.y;
                    Var a: Int = x;
                }
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_002_redeclare_variable_with_constant(self):
        input = """
            Class A {
                Var x, y: Int = 1, 1;
                method(a,b: Int) {
                    Val x, y : Int = 1, 2;
                    Var x: Int = a;
                }
            }
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_003_redeclare_constant(self):
        input = """
            Class A {
                Val x, y: Int = 1, 1;
                method(a,b: Int) {
                    Val x, y : Int = 1, 1;                    
                    Val x: Int = 1;
                    
                }
            }
        """
        expect = "Redeclared Constant: x"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_004_redeclare_constant_with_param(self):
        input = """
            Class A {
                Val x, y: Int = 1, 1;
                method(a,b: Int) {
                    Var x, y : Int = Self.x, Self.y;
                    Val a: Int = 1;
                }
            }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_005_redeclare_constant_with_variable(self):
        input = """
            Class A {
                Val x, y: Int = 1, 1;
                method(a,b: Int) {
                    Var x, y : Int = Self.x, Self.y;
                    Val x: Int = 1;
                }
            }
        """
        expect = "Redeclared Constant: x"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_006_redeclare_attribute_same_type(self):
        input = """
            Class A {
                Val x, y: Int = 1, 1;
                Val x: Int = 1;
            }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_007_redeclare_attribute_different_type(self):
        input = """
            Class A {
                Val x, y: Int = 1, 1;
                Var x: Int = 1;
            }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_008_redeclare_attribute_with_method(self):
        input = """
            Class A {
                x() {}
                Val x, y: Int = 1, 1;
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_009_redeclare_class(self):
        input = """
            Class A {}
            Class A {}
        """
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_010_redeclare_method(self):
        input = """
            Class A {
                method() {}
                method() {}
            }
        """
        expect = "Redeclared Method: method"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_011_redeclare_method_with_attribute(self):
        input = """
            Class A {
                Var x: Int;
                x() {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_012_redeclare_parameter(self):
        input = """
            Class A {
                method(a,a: Int) {}
            }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_013_attribute_inheritance(self):
        input = """
            Class Object {
                Var a, b : Int = 1, 2;
            }
            Class A : Object {
                method() {
                    Var x, y : Int = Self.a, Self.b; ## OK ##
                    Var m, n : Int = m, n; 
                }
            }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_014_multi_layer_inheritance(self):
        input = """
            Class A {
                Var a: Int  = 1;
            }
            Class B : A {
                Var b: Int = 1;
            }
            Class C: B {
                Var c: Int = 1;
                method() {
                    Var a_1, a_2, a_3 : Int = Self.a, Self.b, Self.c;
                    Var x_1 : Int = x;
                }
            }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_015_inheritance_undeclare_class(self):
        input = """
            Class A {
                Var x: Int = 1;
                method(x: Int) {}
            }
            Class B : A {
                Var a: A;
                method(x: A) {}
            }
            Class C: Object {}
        """
        expect = "Undeclared Class: Object"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_016_undeclare_indentifier(self):
        input = """
            Class A {
                Var x, y: Int = 1, 1;
                Var a, b: Int = Self.x, Self.y; 
                method(a,b: Int) {
                    Var x1 : Int = Self.x;
                    Var y1 : Int = Self.y;
                    Var a1 : Int = Self.a;
                    Var b1 : Int = Self.b;
                    Var c1 : Int = c;
                }
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_017_undeclare_attribute(self):
        input = """
            Class A {
                Var x, y: Int = 1, 1;
                Var a, b: Int = Self.x, Self.y;
                Var m, n: Int = p, q; 
                method(a,b: Int) {}
            }
        """
        expect = "Undeclared Identifier: p"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_018_use_declaring_attribute_in_init(self):
        input = """
            Class Program {
                Var a: Int = a;
                main() {}
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_019_use_declaring_self_attribute_in_init(self):
        input = """
            Class Program {
                Var a: Int = Self.a;
                main() {}
            }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_020_access_field_directly(self):
        input = """
            Class Program {
                Var a : Int = 1;
                Var b : Int = Self.a; 
                Var c : Int = a;
                main() {}
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_021_no_entry_point_1(self):
        input = """
            Class Object {main() {}}
            Class ABC {
                main() {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_022_no_entry_point_2(self):
        input = """
            Class Object {main(){}}
            Class Program {
                main(x: Int) {}
                main() {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_023_call_static_attribute_as_method(self):
        input = r"""
            Class Object {
                Var a: Int;
                Var $o: Object;
                method() {
                    Return New Object();
                }
                $method() {
                    Return New Object();
                }
            }
            Class Program : Object {
                main() {
                    Var o: Object = New Object();
                    o = Object::$a();
                }
            }
        """
        expect = "Undeclared Method: $a"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_024_unary_op_1(self):
        input = """
            Class Program {
                Var x: Int = - True;
                main() {}
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_025_unary_op_2(self):
        input = """
            Class Program {
                Var x: Int = - "String";
                main() {}
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,StringLit(String))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_026_unary_op_3(self):
        input = """
            Class Program {
                main() {
                    Var a: Int = 1;
                    Var b: Int = - a;
                    Var c: Float = 1.2;
                    Var d: Float = - 1.2;
                    Var e: Float = - c;
                    Var x: Boolean = True;
                    Var y: Int = - x;
                }
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_027_unary_op_4(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Class_type = New Class_type();
                    Var y: Int = - x;
                }
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_028_unary_op_5(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Boolean = True;
                    Var y: Boolean = ! True;
                    Var z: Boolean = ! x;
                    Var m: Boolean = ! 1; 
                }
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_029_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Int = 1 + 2;
                    Var y: Float = 1 + 1.2;
                    Var m: Int = x + 3;
                    Var n: Float = y + 1.2;
                    Var z: Float = x + y;
                    Var t: Int = m + x;
                    
                    Var a: String;
                    Var b: String = a +. "String";
                    Var c: String = a + "String";
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLit(String))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_030_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Int = 1 - 2;
                    Var y: Float = 1 - 1.2;
                    Var m: Int = x - 3;
                    Var n: Float = y - 1.2;
                    Var z: Float = x - y;
                    Var t: Int = m - x;
                    
                    Var a: Int = 1 - True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_031_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Int = 1 * 2;
                    Var y: Float = 1 * 1.2;
                    Var m: Int = x * 3;
                    Var n: Float = y * 1.2;
                    Var z: Float = x * y;
                    Var t: Int = m * x;
       
                    Var a: Int = 1 * True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_032_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Float = 1 / 2;
                    Var y: Float = 1 / 1.2;
                    Var m: Float = x / 3;
                    Var n: Float = y / 1.2;
                    Var z: Float = x / y;
                    Var t: Float = m / x;
       
                    Var a: Float = 1 / True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_033_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a: Int = 1;
                    Var b: Int = 1;
                    Var x: Int = 1 % 1;
                    Var y: Int = a % 1;
                    Var z: Int = a % b;

                    Var m: Int = 1 % 1.2;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,IntLit(1),FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_034_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a: Boolean = True;
                    Var b: Boolean = False;
                    Var x: Boolean = True && False;
                    Var y: Boolean = True && a;
                    Var z: Boolean = a && b;

                    Var m: Boolean = 1 && True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_035_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a: Boolean = True;
                    Var b: Boolean = False;
                    Var x: Boolean = True || False;
                    Var y: Boolean = True || a;
                    Var z: Boolean = a || b;

                    Var m: Boolean = 1 || True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_036_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a: String = "abc";
                    Var b: String = "abc";
                    Var c: String = "abc" +. "abc";
                    Var d: String = a +. "abc";
                    Var e: String = a +. b;

                    Var f: String = a +. 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_037_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a: String = "abc";
                    Var b: String = "abc";
                    Var c: Boolean = "abc" ==. "abc";
                    Var d: Boolean = a ==. "abc";
                    Var e: Boolean = a ==. b;

                    Var f: Boolean = a ==. 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_038_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a: Boolean = True;
                    Var b: Boolean = False;
                    Var c: Boolean = True == False;
                    Var d: Boolean = a == True;
                    Var e: Boolean = a == b;

                    Var f: Boolean = a == 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_039_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a_1: Boolean = True;
                    Var b_1: Boolean = False;
                    Var c_1: Boolean = True == False;
                    Var d_1: Boolean = a_1 == True;
                    Var e_1: Boolean = a_1 == b_1;

                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 == 1;
                    Var d_2: Boolean = a_2 == 1;
                    Var e_2: Boolean = a_2 == b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 == 1.2;
                    Var d_3: Boolean = a_3 == 1.2;
                    Var e_3: Boolean = a_3 == b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 == 1.2;
                    Var d_4: Boolean = a_4 == 1.2;
                    Var e_4: Boolean = a_4 == b_4;

                    Var f: Boolean = True == 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLit(1.2),FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_040_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a_1: Boolean = True;
                    Var b_1: Boolean = False;
                    Var c_1: Boolean = True != False;
                    Var d_1: Boolean = a_1 != True;
                    Var e_1: Boolean = a_1 != b_1;

                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 != 1;
                    Var d_2: Boolean = a_2 != 1;
                    Var e_2: Boolean = a_2 != b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 != 1.2;
                    Var d_3: Boolean = a_3 != 1.2;
                    Var e_3: Boolean = a_3 != b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 != 1.2;
                    Var d_4: Boolean = a_4 != 1.2;
                    Var e_4: Boolean = a_4 != b_4;

                    Var f: Boolean = True != 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,FloatLit(1.2),FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_041_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 > 1;
                    Var d_2: Boolean = a_2 > 1;
                    Var e_2: Boolean = a_2 > b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 > 1.2;
                    Var d_3: Boolean = a_3 > 1.2;
                    Var e_3: Boolean = a_3 > b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 > 1.2;
                    Var d_4: Boolean = a_4 > 1.2;
                    Var e_4: Boolean = a_4 > b_4;

                    Var f: Boolean = 1 > True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_042_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 >= 1;
                    Var d_2: Boolean = a_2 >= 1;
                    Var e_2: Boolean = a_2 >= b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 >= 1.2;
                    Var d_3: Boolean = a_3 >= 1.2;
                    Var e_3: Boolean = a_3 >= b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 >= 1.2;
                    Var d_4: Boolean = a_4 >= 1.2;
                    Var e_4: Boolean = a_4 >= b_4;

                    Var f: Boolean = 1 >= True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>=,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_043_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 < 1;
                    Var d_2: Boolean = a_2 < 1;
                    Var e_2: Boolean = a_2 < b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 < 1.2;
                    Var d_3: Boolean = a_3 < 1.2;
                    Var e_3: Boolean = a_3 < b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 < 1.2;
                    Var d_4: Boolean = a_4 < 1.2;
                    Var e_4: Boolean = a_4 < b_4;

                    Var f: Boolean = 1 < True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_044_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 <= 1;
                    Var d_2: Boolean = a_2 <= 1;
                    Var e_2: Boolean = a_2 <= b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 <= 1.2;
                    Var d_3: Boolean = a_3 <= 1.2;
                    Var e_3: Boolean = a_3 <= b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 <= 1.2;
                    Var d_4: Boolean = a_4 <= 1.2;
                    Var e_4: Boolean = a_4 <= b_4;

                    Var f: Boolean = 1 <= True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_045_new_expression(self):
        input = """
            Class Object {}
            Class Program {
                main() {
                    Var o: Object = New Object();
                    Var e: Object = New E();
                }
            }
        """
        expect = "Undeclared Class: E"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_046_new_expression_with_constructor(self):
        input = """
            Class Object {
                Constructor() {}
            }
            Class Program {
                main() {
                    Var o: Object = New Object();
                    Var e: Object = New Object(1);
                }
            }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Object),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_047_new_expression_with_constructor_and_coercion(self):
        input = """
            Class Base {}
            Class Sub: Base {}
            Class Object {
                Constructor(x: Float; y: Base) {}
            }
            Class Program {
                main() {
                    Var o_1: Object = New Object(1.2, New Base());
                    Var o_2: Object = New Object(1.2, New Sub());
                    Var o_3: Object = New Object(1, New Base());
                    Var o_4: Object = New Object(1, New Sub());

                    Var o : Object = New Object(1, 1);
                }
            }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Object),[FloatLit(1.2),NewExpr(Id(Sub),[])])"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_048_new_expression_without_constructor(self):
        input = """
            Class Object {}
            Class Program {
                main() {
                    Var o_1: Object = New Object();
                    Var o_2: Object = New Object(1);
                }
            }
        """
        expect = "Undeclared Method: Constructor"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_049_default_constructor_and_user_define_constructor(self):
        input = """
            Class Object {
                Constructor(x: Int) {}
            }
            Class Program {
                main() {
                    Var a: Object = Null;
                    Var b: Object = New Object();
                    Var c: Object = New Object(1);
                    Var d: Object = New Object(1, 2);
                }
            }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Object),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_050_array_cell_simple(self):
        input = """
            Class Program {
                main() {
                    Var a: Array[Int, 3] = Array(1,2,3);
                    a[0] = 1;
                    a[1] = 2;
                    a[a[a[0]]] = 1;
                    a[0][0] = 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(0),IntLit(0)])"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_051_redeclare_variable_with_parameter(self):
        input = """
            Class A {
                Var x, y: Int = 1, 1;
                method(a,b: Int) {
                    Var x, y : Int = Self.x, Self.y;
                    Var a: Int = x;
                }
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_052_redeclare_variable_with_constant(self):
        input = """
            Class A {
                Var x, y: Int = 1, 1;
                method(a,b: Int) {
                    Val x, y : Int = 1, 2;
                    Var x: Int = a;
                }
            }
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_053_redeclare_constant(self):
        input = """
            Class A {
                Val x, y: Int = 1, 1;
                method(a,b: Int) {
                    Val x, y : Int = 1, 1;                    
                    Val x: Int = 1;
                    
                }
            }
        """
        expect = "Redeclared Constant: x"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_054_redeclare_constant_with_param(self):
        input = """
            Class A {
                Val x, y: Int = 1, 1;
                method(a,b: Int) {
                    Var x, y : Int = Self.x, Self.y;
                    Val a: Int = 1;
                }
            }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_055_redeclare_constant_with_variable(self):
        input = """
            Class A {
                Val x, y: Int = 1, 1;
                method(a,b: Int) {
                    Var x, y : Int = Self.x, Self.y;
                    Val x: Int = 1;
                }
            }
        """
        expect = "Redeclared Constant: x"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_056_redeclare_attribute_same_type(self):
        input = """
            Class A {
                Val x, y: Int = 1, 1;
                Val x: Int = 1;
            }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_057_redeclare_attribute_different_type(self):
        input = """
            Class A {
                Val x, y: Int = 1, 1;
                Var x: Int = 1;
            }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_058_redeclare_attribute_with_method(self):
        input = """
            Class A {
                x() {}
                Val x, y: Int = 1, 1;
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_059_redeclare_class(self):
        input = """
            Class A {}
            Class A {}
        """
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_060_redeclare_method(self):
        input = """
            Class A {
                method() {}
                method() {}
            }
        """
        expect = "Redeclared Method: method"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_061_redeclare_method_with_attribute(self):
        input = """
            Class A {
                Var x: Int;
                x() {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_062_redeclare_parameter(self):
        input = """
            Class A {
                method(a,a: Int) {}
            }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_063_attribute_inheritance(self):
        input = """
            Class Object {
                Var a, b : Int = 1, 2;
            }
            Class A : Object {
                method() {
                    Var x, y : Int = Self.a, Self.b; ## OK ##
                    Var m, n : Int = m, n; 
                }
            }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_064_multi_layer_inheritance(self):
        input = """
            Class A {
                Var a: Int  = 1;
            }
            Class B : A {
                Var b: Int = 1;
            }
            Class C: B {
                Var c: Int = 1;
                method() {
                    Var a_1, a_2, a_3 : Int = Self.a, Self.b, Self.c;
                    Var x_1 : Int = x;
                }
            }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_065_inheritance_undeclare_class(self):
        input = """
            Class A {
                Var x: Int = 1;
                method(x: Int) {}
            }
            Class B : A {
                Var a: A;
                method(x: A) {}
            }
            Class C: Object {}
        """
        expect = "Undeclared Class: Object"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_066_undeclare_indentifier(self):
        input = """
            Class A {
                Var x, y: Int = 1, 1;
                Var a, b: Int = Self.x, Self.y; 
                method(a,b: Int) {
                    Var x1 : Int = Self.x;
                    Var y1 : Int = Self.y;
                    Var a1 : Int = Self.a;
                    Var b1 : Int = Self.b;
                    Var c1 : Int = c;
                }
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_067_undeclare_attribute(self):
        input = """
            Class A {
                Var x, y: Int = 1, 1;
                Var a, b: Int = Self.x, Self.y;
                Var m, n: Int = p, q; 
                method(a,b: Int) {}
            }
        """
        expect = "Undeclared Identifier: p"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_068_use_declaring_attribute_in_init(self):
        input = """
            Class Program {
                Var a: Int = a;
                main() {}
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_069_use_declaring_self_attribute_in_init(self):
        input = """
            Class Program {
                Var a: Int = Self.a;
                main() {}
            }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_070_access_field_directly(self):
        input = """
            Class Program {
                Var a : Int = 1;
                Var b : Int = Self.a; 
                Var c : Int = a;
                main() {}
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_071_no_entry_point_1(self):
        input = """
            Class Object {main() {}}
            Class ABC {
                main() {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_072_no_entry_point_2(self):
        input = """
            Class Object {main(){}}
            Class Program {
                main(x: Int) {}
                main() {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test_073_call_static_attribute_as_method(self):
        input = r"""
            Class Object {
                Var a: Int;
                Var $o: Object;
                method() {
                    Return New Object();
                }
                $method() {
                    Return New Object();
                }
            }
            Class Program : Object {
                main() {
                    Var o: Object = New Object();
                    o = Object::$a();
                }
            }
        """
        expect = "Undeclared Method: $a"
        self.assertTrue(TestChecker.test(input, expect, 473))
    

    def test_074_unary_op_1(self):
        input = """
            Class Program {
                Var x: Int = - True;
                main() {}
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_075_unary_op_2(self):
        input = """
            Class Program {
                Var x: Int = - "String";
                main() {}
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,StringLit(String))"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_076_unary_op_3(self):
        input = """
            Class Program {
                main() {
                    Var a: Int = 1;
                    Var b: Int = - a;
                    Var c: Float = 1.2;
                    Var d: Float = - 1.2;
                    Var e: Float = - c;
                    Var x: Boolean = True;
                    Var y: Int = - x;
                }
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_077_unary_op_4(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Class_type = New Class_type();
                    Var y: Int = - x;
                }
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_078_unary_op_5(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Boolean = True;
                    Var y: Boolean = ! True;
                    Var z: Boolean = ! x;
                    Var m: Boolean = ! 1; 
                }
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_079_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Int = 1 + 2;
                    Var y: Float = 1 + 1.2;
                    Var m: Int = x + 3;
                    Var n: Float = y + 1.2;
                    Var z: Float = x + y;
                    Var t: Int = m + x;
                    
                    Var a: String;
                    Var b: String = a +. "String";
                    Var c: String = a + "String";
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLit(String))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_080_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Int = 1 - 2;
                    Var y: Float = 1 - 1.2;
                    Var m: Int = x - 3;
                    Var n: Float = y - 1.2;
                    Var z: Float = x - y;
                    Var t: Int = m - x;
                    
                    Var a: Int = 1 - True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_081_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Int = 1 * 2;
                    Var y: Float = 1 * 1.2;
                    Var m: Int = x * 3;
                    Var n: Float = y * 1.2;
                    Var z: Float = x * y;
                    Var t: Int = m * x;
       
                    Var a: Int = 1 * True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_082_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var x: Float = 1 / 2;
                    Var y: Float = 1 / 1.2;
                    Var m: Float = x / 3;
                    Var n: Float = y / 1.2;
                    Var z: Float = x / y;
                    Var t: Float = m / x;
       
                    Var a: Float = 1 / True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_083_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a: Int = 1;
                    Var b: Int = 1;
                    Var x: Int = 1 % 1;
                    Var y: Int = a % 1;
                    Var z: Int = a % b;

                    Var m: Int = 1 % 1.2;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,IntLit(1),FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_084_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a: Boolean = True;
                    Var b: Boolean = False;
                    Var x: Boolean = True && False;
                    Var y: Boolean = True && a;
                    Var z: Boolean = a && b;

                    Var m: Boolean = 1 && True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_085_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a: Boolean = True;
                    Var b: Boolean = False;
                    Var x: Boolean = True || False;
                    Var y: Boolean = True || a;
                    Var z: Boolean = a || b;

                    Var m: Boolean = 1 || True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_086_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a: String = "abc";
                    Var b: String = "abc";
                    Var c: String = "abc" +. "abc";
                    Var d: String = a +. "abc";
                    Var e: String = a +. b;

                    Var f: String = a +. 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_087_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a: String = "abc";
                    Var b: String = "abc";
                    Var c: Boolean = "abc" ==. "abc";
                    Var d: Boolean = a ==. "abc";
                    Var e: Boolean = a ==. b;

                    Var f: Boolean = a ==. 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_088_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a: Boolean = True;
                    Var b: Boolean = False;
                    Var c: Boolean = True == False;
                    Var d: Boolean = a == True;
                    Var e: Boolean = a == b;

                    Var f: Boolean = a == 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_089_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a_1: Boolean = True;
                    Var b_1: Boolean = False;
                    Var c_1: Boolean = True == False;
                    Var d_1: Boolean = a_1 == True;
                    Var e_1: Boolean = a_1 == b_1;

                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 == 1;
                    Var d_2: Boolean = a_2 == 1;
                    Var e_2: Boolean = a_2 == b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 == 1.2;
                    Var d_3: Boolean = a_3 == 1.2;
                    Var e_3: Boolean = a_3 == b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 == 1.2;
                    Var d_4: Boolean = a_4 == 1.2;
                    Var e_4: Boolean = a_4 == b_4;

                    Var f: Boolean = True == 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLit(1.2),FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_090_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a_1: Boolean = True;
                    Var b_1: Boolean = False;
                    Var c_1: Boolean = True != False;
                    Var d_1: Boolean = a_1 != True;
                    Var e_1: Boolean = a_1 != b_1;

                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 != 1;
                    Var d_2: Boolean = a_2 != 1;
                    Var e_2: Boolean = a_2 != b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 != 1.2;
                    Var d_3: Boolean = a_3 != 1.2;
                    Var e_3: Boolean = a_3 != b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 != 1.2;
                    Var d_4: Boolean = a_4 != 1.2;
                    Var e_4: Boolean = a_4 != b_4;

                    Var f: Boolean = True != 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,FloatLit(1.2),FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_091_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 > 1;
                    Var d_2: Boolean = a_2 > 1;
                    Var e_2: Boolean = a_2 > b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 > 1.2;
                    Var d_3: Boolean = a_3 > 1.2;
                    Var e_3: Boolean = a_3 > b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 > 1.2;
                    Var d_4: Boolean = a_4 > 1.2;
                    Var e_4: Boolean = a_4 > b_4;

                    Var f: Boolean = 1 > True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_092_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 >= 1;
                    Var d_2: Boolean = a_2 >= 1;
                    Var e_2: Boolean = a_2 >= b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 >= 1.2;
                    Var d_3: Boolean = a_3 >= 1.2;
                    Var e_3: Boolean = a_3 >= b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 >= 1.2;
                    Var d_4: Boolean = a_4 >= 1.2;
                    Var e_4: Boolean = a_4 >= b_4;

                    Var f: Boolean = 1 >= True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>=,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_093_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 < 1;
                    Var d_2: Boolean = a_2 < 1;
                    Var e_2: Boolean = a_2 < b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 < 1.2;
                    Var d_3: Boolean = a_3 < 1.2;
                    Var e_3: Boolean = a_3 < b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 < 1.2;
                    Var d_4: Boolean = a_4 < 1.2;
                    Var e_4: Boolean = a_4 < b_4;

                    Var f: Boolean = 1 < True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_094_binary_op(self):
        input = """
            Class Class_type {}
            Class Program {
                main() {
                    Var a_2: Int = 1;
                    Var b_2: Int = 1;
                    Var c_2: Boolean = 1 <= 1;
                    Var d_2: Boolean = a_2 <= 1;
                    Var e_2: Boolean = a_2 <= b_2;

                    Var a_3: Float = 1.2;
                    Var b_3: Float = 1.2;
                    Var c_3: Boolean = 1.2 <= 1.2;
                    Var d_3: Boolean = a_3 <= 1.2;
                    Var e_3: Boolean = a_3 <= b_3; 

                    Var a_4: Int = 1;
                    Var b_4: Float = 1.2;
                    Var c_4: Boolean = 1 <= 1.2;
                    Var d_4: Boolean = a_4 <= 1.2;
                    Var e_4: Boolean = a_4 <= b_4;

                    Var f: Boolean = 1 <= True;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_095_new_expression(self):
        input = """
            Class Object {}
            Class Program {
                main() {
                    Var o: Object = New Object();
                    Var e: Object = New E();
                }
            }
        """
        expect = "Undeclared Class: E"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_096_new_expression_with_constructor(self):
        input = """
            Class Object {
                Constructor() {}
            }
            Class Program {
                main() {
                    Var o: Object = New Object();
                    Var e: Object = New Object(1);
                }
            }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Object),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_097_new_expression_with_constructor_and_coercion(self):
        input = """
            Class Base {}
            Class Sub: Base {}
            Class Object {
                Constructor(x: Float; y: Base) {}
            }
            Class Program {
                main() {
                    Var o_1: Object = New Object(1.2, New Base());
                    Var o_2: Object = New Object(1.2, New Sub());
                    Var o_3: Object = New Object(1, New Base());
                    Var o_4: Object = New Object(1, New Sub());

                    Var o : Object = New Object(1, 1);
                }
            }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Object),[FloatLit(1.2),NewExpr(Id(Sub),[])])"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_098_new_expression_without_constructor(self):
        input = """
            Class Object {}
            Class Program {
                main() {
                    Var o_1: Object = New Object();
                    Var o_2: Object = New Object(1);
                }
            }
        """
        expect = "Undeclared Method: Constructor"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_099_default_constructor_and_user_define_constructor(self):
        input = """
            Class Object {
                Constructor(x: Int) {}
            }
            Class Program {
                main() {
                    Var a: Object = Null;
                    Var b: Object = New Object();
                    Var c: Object = New Object(1);
                    Var d: Object = New Object(1, 2);
                }
            }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Object),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 499))
    
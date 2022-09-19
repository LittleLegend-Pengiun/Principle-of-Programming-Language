// Họ tên: Lê Hoàng Anh
// MSSV: 1910752
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: class_declaration+ EOF;


// Parser start here
//================================================================
// 2. Program structure
// 2.1 Class delcaration
class_declaration: CLASS NORMAL_ID (COLLON NORMAL_ID)? LP list_of_members RP;

list_of_members: member*;
member: attribute_declaration | method_declaration;

// 2.2 Attribute declaration
attribute_declaration: (VAL | VAR) (attr_decl_bis | attr_decl_bis1) SEMI;
attr_decl_bis: possible_id COLLON type_name EQU expression 
			 | possible_id COMMA attr_decl_bis COMMA expression;
attr_decl_bis1: id_list_attribute COLLON type_name;
possible_id: NORMAL_ID | DOLLAR_ID;
id_list_attribute: possible_id more_id_attribute | possible_id;
more_id_attribute: COMMA id_list_attribute;

value_list: list_of_expressions;
type_name: array_type | INT | FLOAT | BOOLEAN | STRING | NORMAL_ID;

// 2.3 Method declaration
method_declaration: normal_method | constructor | destructor ;
normal_method: possible_id LB list_of_parameters? RB block_stmt;
//main_method: 'main' LB RB block_stmt;
constructor: CONSTRUCTOR LB list_of_parameters? RB block_stmt;
destructor: DESTRUCTOR LB RB block_stmt;

list_of_parameters: parameters more_parameters | parameters;
more_parameters: SEMI list_of_parameters;
parameters: id_list COLLON type_name;
id_list: NORMAL_ID more_id | NORMAL_ID;
more_id: COMMA id_list;

// 5. Expression
list_of_expressions: expression more_expression | expression;
more_expression: COMMA list_of_expressions;

expression: string_expression;
string_expression: expr1 (STR_ADD | STR_EQ) expr1
				 | expr1;

expr1: relation_expression;
relation_expression: expr2 (DOUBLE_EQU | DIF | SMALLER | BIGGER | 
							SMA_EQ | BIG_EQ) expr2
				   | expr2;

expr2: logical_expression;
logical_expression: logical_expression (AND | OR) expr3
				  | expr3;

expr3: adding_expression;
adding_expression: adding_expression (ADD | SUB) expr4
				 | expr4;

expr4: multiplying_expression;
multiplying_expression: multiplying_expression (MUL | DIV | MOD) expr5
					  | expr5;

expr5: not_expression;
not_expression: NOT expr5
			  | expr6;

expr6: negative_expression;
negative_expression: SUB expr6
				   | expr7;

expr7: index_expression;
index_expression: index_expression LSB expression RSB
				| expr8;

expr8: object_access_expression;
object_access_expression: object_access_expression DOT NORMAL_ID
						  (LB list_of_expressions? RB)?
						  | static_ob_access
						  | static_mth_access
						  | expr9;

expr9: object_creation_expression
	 | operand;

operand: all_literals
		| NORMAL_ID
		| SELF
		| LB expression RB;


all_literals: all_int_lit | FLOAT_LIT | STR_LIT | BOOL_LIT | array_lit | NULL;
/* 5.6. Member access */
inst_ob_access: object_access_expression DOT NORMAL_ID;
inst_mth_access: super_inst_mth_acess DOT NORMAL_ID LB list_of_expressions? RB;
super_inst_mth_acess: super_inst_mth_acess DOT NORMAL_ID
					(LB list_of_expressions? RB)?
					| static_ob_access
					| static_mth_access
					| expr9;

static_ob_access: NORMAL_ID DOUBLE_COLON DOLLAR_ID;
static_mth_access: NORMAL_ID DOUBLE_COLON DOLLAR_ID LB list_of_expressions? RB;

// 5.7. Object creation
object_creation_expression: NEW NORMAL_ID LB list_of_expressions? RB;


// 6. Statements
//===============================================================
statements: var_and_const_stmt
			| assign_stmt 
			| if_stmt 
			| for_in_stmt
			| break_stmt 
			| cont_stmt 
			| return_stmt 
			| method_invocation_stmt;

var_and_const_stmt: (VAL | VAR) (var_and_const_bis | var_and_const_bis1) SEMI;
var_and_const_bis: NORMAL_ID COLLON type_name EQU expression 
			 | NORMAL_ID COMMA var_and_const_bis COMMA expression;
var_and_const_bis1: NORMAL_ID (COMMA NORMAL_ID)* COLLON type_name;

assign_stmt: left_hand_side EQU expression SEMI;
left_hand_side: index_expression LSB expression RSB
			  | scalar_var;
scalar_var: NORMAL_ID | inst_ob_access | static_ob_access;

if_stmt: IF LB expression RB block_stmt 
		(ELSEIF LB expression RB block_stmt)*
		(ELSE block_stmt)?;
for_in_stmt: FOREACH LB expression IN expression DOUBLE_DOT expression (BY expression)? RB block_stmt;
break_stmt: BREAK SEMI;
cont_stmt: CONTINUE SEMI;
return_stmt: RETURN expression? SEMI;
method_invocation_stmt: (inst_mth_access | static_mth_access) SEMI;
block_stmt: LP statements* RP;

// Lexer start here
//================================================================
/* Lexer Literal: 5 + 6. Indexed Array */
array_lit: indexed_array | multi_demensional_array;
indexed_array: ARRAY LB list_of_expressions? RB ;
multi_demensional_array: ARRAY LB list_of_arrays RB;

list_of_arrays: indexed_array more_array | indexed_array;
more_array: COMMA list_of_arrays;

// Array type
array_type: ARRAY LSB type_name COMMA INT_LIT RSB;

all_int_lit: INT_LIT | ZERO;

// TRUE Lexer begins
//================================================================
/* Keywords 
		Must begin with a uppercase letter.
*/
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
fragment TRUE: 'True';
fragment FALSE: 'False';
ARRAY: 'Array';
IN: 'In';
INT: 'Int'; 
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
RETURN: 'Return';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';
SELF: 'Self';

/* Operators */
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
DOUBLE_EQU: '==';
EQU: '=';
DIF: '!=';
SMALLER: '<';
SMA_EQ: '<=';
BIGGER: '>';
BIG_EQ: '>=';
STR_EQ: '==.';
STR_ADD: '+.';
DOT: '.';
DOUBLE_DOT: '..';
COLLON: ':';
DOUBLE_COLON: '::';
// New is determined above

/* Separator */
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
COMMA: ',';
SEMI: ';';
LP: '{';
RP: '}';

/* Literals
1. Interger: */
ZERO: (('0x' | '0X' | '0b' | '0B'| '0')? '0') {
	self.text = str(self.text).replace("_", "")
};
fragment OCT_INTEGER_LITERAL: '0'[1-7]('_'? [0-7])*;
fragment HEX_INTEGER_LITERAL: ('0x' | '0X') [1-9A-F] ('_'? [0-9] | '_'? [A-F])*;
fragment BIN_INTEGER_LITERAL: ('0b' | '0B') '1' ('_'? '0' | '_'? '1')*;
fragment DEC_INTEGER_LITERAL: [1-9] (([0-9] | '_')? [0-9])*;
INT_LIT: ( OCT_INTEGER_LITERAL
		 | HEX_INTEGER_LITERAL
		 | BIN_INTEGER_LITERAL
		 | DEC_INTEGER_LITERAL ) {
	self.text = str(self.text).replace("_", "")
};

/* 
2. Float: */
fragment INTEGER_PART_LITERAL: ([1-9] (([0-9] | '_')? [0-9])* | '0');
fragment DECIMAL_PART_LITERAL: '.' [0-9]*;
fragment EXPONENT_PART_LITERAL: ('e' | 'E') ('-' | '+')? [0-9]+;
FLOAT_LIT: (INTEGER_PART_LITERAL DECIMAL_PART_LITERAL EXPONENT_PART_LITERAL?
		 | INTEGER_PART_LITERAL EXPONENT_PART_LITERAL
		 | DECIMAL_PART_LITERAL EXPONENT_PART_LITERAL) {
	self.text = str(self.text).replace("_", "")
};

/*
3. Boolean: */
BOOL_LIT: TRUE | FALSE;

/* Identifier */
//fragment ID: ([a-zA-Z] | '_') ([a-zA-Z] | [0-9] | '_')*;
DOLLAR_ID: '$' ([a-zA-Z] | [0-9] | '_')+;
NORMAL_ID: ([a-zA-Z] | '_') ([a-zA-Z] | [0-9] | '_')*;

/* Comment */
COMMENT: '##' .*? '##' -> skip;

/*
4. String: */
STR_LIT: ('"' ('\''? CHAR)* '"') { self.text = self.text[1:-1] };
fragment CHAR: ~[\b\t\n\f\r'"\\] | ESC_SEQ | '\'"';
fragment ESC_SEQ: '\\' ('b'|'t'|'n'|'f'|'r'|'\\'|'\'');
fragment ILLEGAL_SEQUENCE: '\\' ~[btnfr'\\] ;


WS: [ \t\r\n\f]+ -> skip; // skip tabs, spaces, newlines, form feeds

ERROR_TOKEN: .{raise ErrorToken(self.text)} ;
UNCLOSE_STRING: ('"' ('\''? CHAR)* '\''*) {raise UncloseString(str(self.text)[1:])} ;
ILLEGAL_ESCAPE: ('"' ('\''? CHAR)* ILLEGAL_SEQUENCE) {
	raise IllegalEscape(self.text[1:])
} ;
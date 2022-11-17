//2013392
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
    language=Python3;
}

program  : class_declaration+ EOF ;

//PROGRAM STRUCTURE
class_declaration: CLASS ID (EXTENDS ID)? LP members* RP;
members: attribute_declare | method_declare;

attribute_declare: mutable_declare | immutable_declare;

mutable_declare: (STATIC| ) type_attribute list_var_declare SEMI;
immutable_declare: (FINAL | STATIC FINAL | FINAL STATIC) type_attribute list_var_declare_immu SEMI;
list_var_declare: var_declare COMMA list_var_declare | var_declare;
list_var_declare_immu: var_declare_immu COMMA list_var_declare_immu | var_declare_immu;

method_declare: ((STATIC|) return_type ID LB list_params RB block_statement) | constructor_declare;
constructor_declare: ID LB list_params RB  block_statement;
var_declare: ID (ASSIGN exp)?;
var_declare_immu: ID ASSIGN exp;
list_params: | parameter (SEMI parameter)* ;
parameter: parameter_type ID (COMMA ID)*;
parameter_type: type_attribute;


//TYPE
return_type: primitive_type | class_type | array_type ;
type_attribute: class_type | primitive_type |  array_type;
array_type: (INT | FLOAT | BOOLEAN | STRING | class_type) LSB INT_LIT RSB;
class_type: ID;
primitive_type: INT | FLOAT | BOOLEAN | STRING | VOID ;


//STATEMENT

block_statement: LP (local_attribute*) (statement*) RP;
local_attribute: type_attribute list_var_declare SEMI
               | FINAL type_attribute list_var_declare_immu SEMI;

statement: block_statement
         | assignment_statement SEMI
         | if_statement
         | for_statement
         | break_statement SEMI
         | continue_statement SEMI
         | return_statement SEMI
         | method_invocation_statement SEMI;


assignment_statement: lhs ASSIGN_EQ exp;
lhs: ID | operands index_exp | attribute_invo DOT ID;
attribute_invo: ID
              | attribute_invo DOT ID list_exp
              | LB exp RB
              | attribute_invo index_exp
              | THIS;

if_statement: IF bool_exp THEN statement (ELSE statement)? ;
for_statement: FOR ID ASSIGN_EQ int_exp (TO | DOWNTO) int_exp DO statement;
break_statement: BREAK ;
continue_statement: CONTINUE;
return_statement: RETURN return_exp ;
method_invocation_statement: obj_methodinvo DOT ID list_exp;
obj_methodinvo: literals 
              | ID  
              | operands DOT ID  
              | operands DOT ID list_exp 
              | LB exp RB  
              | operands index_exp  
              | THIS 
              | NIL;


//EXPRESSION
bool_exp: exp;
int_exp: exp;
return_exp: exp;
exp: exp1 (LT | GT | LTE | GTE ) exp1 | exp1;
exp1: exp2 (EQ | NEQ) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 ( MUL | FLOAT_DIV | INT_DIV | MOD ) exp5 | exp5;
exp5: exp5 CONCAT exp6 | exp6;
exp6: NOT exp6 | exp7;
exp7: (ADD | SUB) exp7 | exp8;
exp8: exp9 LSB exp RSB | exp9;
exp9: exp9 DOT exp10 | exp10;
exp10: operands NEW exp10 | operands;
operands: literals
        | ID
        | operands index_exp
        | operands DOT ID
        | operands DOT ID list_exp
        | LB exp RB
        | object_create
        | THIS
        | NIL
        | TRUE
        | FALSE;

index_exp: LSB exp RSB;
object_create: NEW ID list_exp;
list_exp: LB list_exps RB;
list_exps:<assoc=right> exp ( COMMA exp )* | ;


//KEYWORD
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
EXTENDS: 'extends';
FLOAT: 'float';
IF: 'if';
INT: 'int';
STRING: 'string';
THEN: 'then' ;
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';

//OPERATOR
ADD: '+';
SUB: '-';
MUL: '*';
FLOAT_DIV: '/';
INT_DIV: '\\';
MOD: '%';
NEQ: '!=';
EQ : '==' ;
LT : '<' ;
GT : '>' ;
LTE: '<=';
GTE: '>=';
OR: '||';
AND: '&&';
NOT: '!';
CONCAT: '^';
NEW: 'new';
ASSIGN: '=';
ASSIGN_EQ: ':=';

//SEPARATOR
LSB:'[';
RSB: ']';
LP: '{';
RP: '}';
LB: '(';
RB: ')';
SEMI: ';';
COLON: ':';
DOT: '.';
COMMA: ',';


//LITERAL
literals: literal_basic | array_literal ;
BOOL_LIT: TRUE | FALSE ;
array_literal: LP list_literal_basic RP;
list_literal_basic: literal_basic COMMA list_literal_basic | literal_basic;
literal_basic: INT_LIT | FLOAT_LIT | STRING_LIT | THIS | NIL | BOOL_LIT;
INT_LIT: [0-9]+;
FLOAT_LIT: FLOAT_LIT_case1 | FLOAT_LIT_case2;
FLOAT_LIT_case1: [0-9]+ ('.' [0-9]*)? ('E' | 'e') ('+' | '-')? [0-9]+;
FLOAT_LIT_case2: [0-9]+ '.' [0-9]*;
STRING_LIT: '"' STR_CHAR* '"'
    {
        y = str(self.text)
        self.text = y
    };




ID: [_a-zA-Z][_a-zA-Z0-9]* ;

COMMENT: (BLOCK_COMMENT|LINE_COMMENT) -> skip;

WS : [ \f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' STR_CHAR*
    {
        y = str(self.text)
        raise UncloseString(y)
    }
    ;

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
    {
        y = str(self.text)
        raise IllegalEscape(y)
    }
    ;

fragment BLOCK_COMMENT: '/*' (.)*? '*/';
fragment LINE_COMMENT: '#' ~[\r\n]*;
fragment STR_CHAR: ( '\\' [btnfr"\\] | ~[\n\r"\\] ) ;
fragment ESC_ILLEGAL: '\\'~[bfrnt"\\]| '\''~'"';


ERROR_CHAR: .
    {
        raise ErrorToken(self.text)
    };

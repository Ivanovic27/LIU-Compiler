grammar Liu;        

program
  : function_code
  ;
function_code
  : (instruction Dot function_code)?
  ;
instruction
  : definition | execution | return_statement
  ;
definition
  : identification Colon extended_literal | definition_function_name Colon function
  ;
identification
  : Id identification2
  ;
identification2
  : (Id identification2)?
  ;
terminal_definition
  : Id Colon basic_literal | definition_function_name Colon function
  ;
execution
  : execution_function_name | if_statement | iterate_statement
  ;
execution_function_name
  : identification group execution_function_name2 | group identification execution_function_name2
  ;
execution_function_name2
  : (identification execution_function_name2 | group execution_function_name2)?
  ;
if_statement
  : If group group else_statement
  ;
else_statement
  : (Else group | Else if_statement )?
  ;
iterate_statement
  : Iterate group group
  ;
return_statement
  : Return group
  ;
definition_function_name
  : identification parameters definition_function_name2 | parameters identification definition_function_name2
  ;
definition_function_name2
  : (identification definition_function_name2 | parameters definition_function_name2)?
  ;
parameters
  : Left_par parameters3 Right_par
  ;
parameters2
  : (Coma definition parameters2 | Coma identification parameters2)?
  ;
parameters3
  : (definition parameters2 | identification  parameters2)?
  ;
extended_literal
  : literal | group
  ;
basic_literal
  : String | Number | Boolean | execution | identification
  ;
literal
  : basic_literal | terminal_definition
  ;
function
  : Left_bracket function_code Right_bracket
  ;
group
  : Left_par group2 Right_par
  ;
group2
  : (literal group3)?
  ;
group3
  : (Coma literal group3)?
  ;


Colon           :':';
Coma            :',';
Left_par        :'(';
Right_par       :')';
Left_bracket    :'{';
Right_bracket   :'}';
Dot             :'.';
Dash            :'-';
If              :'if';
Else            :'else';
Iterate         :'iterate';
Return          :'return';
Boolean         :'True'|'False';


Id
 : [a-zA-Z_] [a-zA-Z_0-9]*
 ;

String
 : ['] ( ~['\r\n\\] | '\\' ~[\r\n] )* [']
 ;

 Ws
 : [ \t\r\n\u000C] -> skip
 ;

 Number
 : ('0'..'9')+ ('.' ('0'..'9')+)?
 ;
  
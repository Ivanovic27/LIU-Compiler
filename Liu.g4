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
  : identification Colon extended_literal | definition_function_name Colon function Colon basic_literal
  ;
identification
  : Id identification2
  ;
identification2
  : (Id identification2)?
  ;

terminal_definition
  : identification Colon basic_literal
  ;
execution
  : if_execution | iterate_execution | add_execution | subtract_execution | divide_execution | multiply_execution | not_execution | equal_execution | greater_execution | less_execution | print_execution | read_execution | or_execution | and_execution | next_execution | execution_function_name
  ;
add_execution
  : Add group
  ;
subtract_execution
  : Subtract group
  ;
divide_execution
  : Divide group
  ;
multiply_execution
  : Multiply group
  ;
if_execution
  : If group function else_execution
  ;
else_execution
  : (Else function | Else if_execution )?
  ;
iterate_execution
  : Iterate group function
  ;
not_execution
  : Not group
  ;
equal_execution
  : Equal group
  ;
greater_execution
  : Greater group
  ;
less_execution
  : Less group
  ;
or_execution
  : Or group
  ;
and_execution
  : And group
  ;
print_execution
  : Print group
  ;
read_execution
  : Read group
  ;
next_execution
  : group Next
  ;
execution_function_name
  : identification group execution_function_name2 | group identification execution_function_name2
  ;
execution_function_name2
  : (identification execution_function_name2 | group execution_function_name2)?
  ;
return_statement
  : Return basic_literal | Return group
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
  : (Coma definition parameters2)?
  ;
parameters3
  : (definition parameters2)?
  ;
extended_literal
  : literal | list1
  ;
basic_literal
  : String | Number | Boolean | execution | identification | Empty
  ;
literal
  : basic_literal | terminal_definition
  ;
function
  : Left_curly_braces function_code Right_curly_braces 
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
list1
  : Left_bracket list2 Right_bracket
  ;
list2
  : (literal list3)?
  ;
list3
  : (Coma literal list3)?
  ;

Empty           :'Empty';
Colon           :':';
Coma            :',';
Left_par        :'(';
Right_par       :')';
Left_curly_braces    :'{';
Right_curly_braces   :'}';
Left_bracket    :'[';
Right_bracket   :']';
Dot             :'.';
Dash            :'-';
Add             : 'add';
Subtract        : 'subtract';
Divide          : 'divide';
Multiply        : 'multiply';
If              : 'if';
Else            : 'else';
Iterate         : 'iterate while';
Not             : 'not';
Equal           : 'equal';
NotEqual        : 'not equal';
Greater         : 'greater';
Less            : 'less';
Print           : 'print';
Read            : 'read';
Boolean         : 'True' | 'False';
Return          : 'return';
Or              : 'or';
And             : 'and';
Next            :'next';


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
  
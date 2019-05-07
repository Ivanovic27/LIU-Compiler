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
  : identification Colon extended_literal | definition_function_name Colon function Colon extended_literal | array_access Colon extended_literal
  ;
identification
  : Id identification2
  ;
identification2
  : (Id identification2)?
  ;
array_access
  : identification array_access2
  ;
array_access2
  : (Left_bracket basic_literal array_access3 Right_bracket)?
  ;
array_access3
  : (Coma basic_literal array_access3)?
  ;

terminal_definition
  : identification Colon basic_literal
  ;
execution
  : if_execution | iterate_execution
  | add_execution | subtract_execution | divide_execution | multiply_execution
  | not_execution | equal_execution | greater_execution | less_execution | min_execution | max_execution
  | print_execution | read_execution | or_execution | and_execution | sqrt_execution | power_execution
  | multiply_all_execution | subtract_all_execution | add_all_execution | first_execution | last_execution
  | is_text_execution | is_number_execution | is_even_execution | is_odd_execution | is_empty_execution
  | map_execution | filter_execution | length_execution
  | execution_function_name
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
sqrt_execution
  : Sqrt group
  ;
power_execution
  : group Power group
  ;
max_execution
  : Max group
  ;
min_execution
  : Min group
  ;
multiply_all_execution
  : group MultiplyAll
  ;
subtract_all_execution
  : group SubtractAll
  ;
add_all_execution
  : group AddAll
  ;
first_execution
  : group First
  ;
last_execution
  : group Last
  ;
is_text_execution
  : group IsText
  ;
is_number_execution
  : group IsNumber
  ;
is_even_execution
  : group IsEven
  ;
is_odd_execution
  : group IsOdd
  ;
is_empty_execution
  : group IsEmpty
  ;
map_execution
  : group Map group
  ;
filter_execution
  : group Filter group
  ;
length_execution
  : group Length
  ;
execution_function_name
  : identification group execution_function_name2 | group identification execution_function_name2
  ;
execution_function_name2
  : (identification execution_function_name2 | group execution_function_name2)?
  ;
return_statement
  : Return basic_literal
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
  : basic_literal | array
  ;
basic_literal
  : String | Number | Boolean | execution | identification | array_access | Empty
  ;
function
  : Left_curly_braces function_code Right_curly_braces 
  ;
group
  : Left_par group2 Right_par
  ;
group2
  : (basic_literal group3)?
  ;
group3
  : (Coma basic_literal group3)?
  ;
array
  : Left_par Number array_dimension Right_par Left_bracket Right_bracket
  ;
array_dimension
  : (Coma Number array_dimension)?
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
Sqrt            : 'sqrt';
Power           : 'power';
Max             : 'max';
Min             : 'min';
MultiplyAll     : 'multiply all';
SubtractAll     : 'subtract all';
AddAll          : 'add all';
First           : 'first';
Last            : 'last';
IsText          : 'is text';
IsNumber        : 'is number';
IsEven          : 'is even';
IsOdd           : 'is odd';
IsEmpty         : 'is empty';
Map             : 'map';
Filter          : 'filter';
Length          : 'length';


Id
 : [a-zA-Z_] [a-zA-Z_0-9]*
 ;

String
 : ['] ( ~['\r\n\\] | '\\' ~[\r\n] )* [']
 ;

 Ws
 : [ \t\r\n\u000C] -> skip
 ;

 Comment
 : '---' .*? '---' -> skip
 ;

 CommentLine
 : '--' ~[\r\n]* -> skip
 ;

 Number
 : [+|-]? ('0'..'9')+ ('.' ('0'..'9')+)?
 ;
  
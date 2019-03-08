grammar Liu;        

 programa
 : Program Id Semicolon programa2
 ;

 programa2
 : (vars1 bloque | bloque)
 ;

 vars1
 : Var id1 Colon tipo Semicolon vars2
 ;

 vars2
 : (id1 Colon tipo Semicolon vars2)?
 ;
 
 id1
 : (Id Coma id1 | Id)
 ;

 tipo
 : (Int | Float)
 ;

 bloque
 : (Open_bracket bloque2 | Open_bracket Close_bracket)
 ;

 bloque2
 : (estatuto bloque2 | estatuto Close_bracket)
 ;

 estatuto
 : (asignacion | condicion | escritura)
 ;

 asignacion
 : Id Equal expresion Semicolon
 ;

 expresion
 : exp expresion2
 ;

 expresion2
 : (Relop exp)?
 ;

 escritura
 : Print Open_parenthesis escritura2 escritura3 Close_parenthesis Semicolon
 ;

 escritura2
 : (expresion | Cte_string)
 ;
 
 escritura3
 : (Coma escritura2 escritura3)?
 ;

 condicion
 : If Open_parenthesis expresion Close_parenthesis bloque condicion2 Semicolon
 ;

 condicion2
 : (Else bloque)?
 ;

 exp
 : termino exp2
 ;

 exp2
 : (Term exp)?
 ;

 termino
 : factor termino2
 ;
 
 termino2
 : (Fac termino)?
 ;

 factor
 : (Open_parenthesis expresion Close_parenthesis |  Term var_cte | var_cte)
 ;

 var_cte
 : (Id | Cte_f | Cte_i)
 ;


Int             : 'int';
Float           : 'float';
If              : 'if';
Else            : 'else';
Program         : 'program';
Print           : 'print';
Var             : 'var';
Semicolon       : ';';
Colon           : ':';
Open_bracket    : '{';
Close_bracket   : '}';
Coma            : ',';
Open_parenthesis    : '(';
Close_parenthesis   : ')';
Equal           : '=';
Relop           : '<'|'>'|'<>';
Fac             : '/'|'*';
Term            : '+'|'-';


Id
 : [a-zA-Z_] [a-zA-Z_0-9]*
 ;

Cte_string
 : ["] ( ~["\r\n\\] | '\\' ~[\r\n] )* ["]
 | ['] ( ~['\r\n\\] | '\\' ~[\r\n] )* [']
 ;

 Ws
 : [ \t\r\n\u000C] -> skip
 ;

 Cte_i
 : ('0'..'9')+
 ;

 Cte_f
 : Cte_i '.' Cte_i
 ;
  
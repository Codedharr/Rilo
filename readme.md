##RILO##

El objetivo del proyecto es desarrollar un lenguaje de programación especializado basado en Python, que facilite al usuario la elaboración de instrucciones precisas para administrar un robot sin necesidad de tener en cuenta los detalles de nivel básico. Este lenguaje busca que el usuario se enfoque en la lógica del movimiento (avance, giro, alteración de velocidades o generación de sonidos) y no en la manipulación directa de controladores motores, sensores o protocolos de comunicación. 

Diseñado por Daniel Rendon
Universidad Valle del Momboy 
Docente. Ing. Katiuska Morillo




<program>      ::= <statement>* 
<statement>    ::= "start()" 
                 | "stop()" 
                 | "move" <space> <direction_fw_bw> <space> <number> 
                 | "run" <space> <number> 
                 | "turn" <space> <direction_lr> 
                 | "sound" <space> <string_lit> 
<direction_fw_bw> ::= "forward" | "backward" 
<direction_lr>     ::= "left"    | "right" 
<number>           ::= digit+ 
<string_lit>       ::= '"' { any_char_except_"}+ '"' 
<space>            ::= " " 
<digit>            ::= "0" | "1" | … | "9" 


📄 Texto → �� Tokens → ��️ AST → �� Robot
   ↓         ↓         ↓        ↓
 Lexer    Parser   Interpreter  Acción

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
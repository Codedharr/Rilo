import re
from errors import LexicalError

# Definición de tokens
TOKEN_SPECIFICATION = [
    ('NUMBER',      r'\d+'),           # Números: 1, 2, 3, 10, 100...
    ('STRING',      r'"[^"]*"'),       # Texto entre comillas: "hola", "beep"
    ('START',       r'start\(\)'),     # Comando: start()
    ('STOP',        r'stop\(\)'),      # Comando: stop()
    ('MOVE',        r'move'),          # Comando: move
    ('RUN',         r'run'),           # Comando: run
    ('TURN',        r'turn'),          # Comando: turn
    ('SOUND',       r'sound'),         # Comando: sound
    ('DIRECTION',   r'forward|backward|left|right'), # Direcciones
    ('LPAREN',      r'\('),            # Paréntesis izquierdo: (
    ('RPAREN',      r'\)'),            # Paréntesis derecho: )
    ('SKIP',        r'[ \t]+'),        # Espacios y tabulaciones
    ('MISMATCH',    r'.'),             # Cualquier otro carácter
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)
_compiled_re = re.compile(token_regex, re.IGNORECASE)

def lex(text, line_num):

    tokens = []
    pos = 0
    while pos < len(text):
        mo = _compiled_re.match(text, pos)
        if not mo:
            break
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise LexicalError(line_num, value)
        else:
            tokens.append((kind, value))
        pos = mo.end()
    return tokens
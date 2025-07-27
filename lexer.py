# lexer.py

import re
from errors import LexicalError

# Definición de tokens y sus patrones regex
TOKEN_SPECIFICATION = [
    ('NUMBER',      r'\d+'),
    ('STRING',      r'"[^"]*"'),
    ('START',       r'start\(\)'),
    ('STOP',        r'stop\(\)'),
    ('MOVE',        r'move'),
    ('RUN',         r'run'),
    ('TURN',        r'turn'),
    ('SOUND',       r'sound'),
    ('DIRECTION',   r'forward|backward|left|right'),
    ('LPAREN',      r'\('),
    ('RPAREN',      r'\)'),
    ('SKIP',        r'[ \t]+'),    # Espacios y tabulaciones
    ('MISMATCH',    r'.'),         # Cualquier otro carácter (error léxico)
]

# Compilar la expresión regular combinada (insensible a mayúsculas/minúsculas)
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)
_compiled_re = re.compile(token_regex, re.IGNORECASE)


def lex(text, line_num):
    """
    Analiza léxicamente una línea de código.
    Devuelve lista de tuplas (TIPO, valor en minúsculas).
    Lanza LexicalError en caso de símbolo inesperado.
    """
    tokens = []
    pos = 0
    while pos < len(text):
        mo = _compiled_re.match(text, pos)
        if not mo:
            break
        kind = mo.lastgroup
        value = mo.group(kind)
        pos = mo.end()

        if kind == 'SKIP':
            continue
        if kind == 'MISMATCH':
            # Símbolo no reconocido -> error léxico
            raise LexicalError(line_num, value)

        # Normalizar a minúsculas para valores
        normalized = value.lower()
        tokens.append((kind, normalized))

    return tokens

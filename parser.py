# parser.py

from errors import SyntacticError
from lexer import lex

class ASTNode:
    def __init__(self, node_type, value=None):
        self.type = node_type
        self.value = value
    def __repr__(self):
        return f"ASTNode({self.type}, {self.value})"


def parse(tokens, line_num):
    if not tokens:
        return None

    t0 = tokens[0][0]
    # start()
    if t0 == 'START' and len(tokens) == 1:
        return ASTNode('START')

    # stop()
    if t0 == 'STOP' and len(tokens) == 1:
        return ASTNode('STOP')

    # move <direction> <number>
    if t0 == 'MOVE':
        if len(tokens) == 3 and tokens[1][0] == 'DIRECTION' and tokens[2][0] == 'NUMBER':
            direction = tokens[1][1].lower()
            distance = int(tokens[2][1])
            return ASTNode('MOVE', (direction, distance))
        raise SyntacticError(line_num, "Sintaxis inválida para 'move'. Debe ser: move <direction> <number>")

    # turn <direction>
    if t0 == 'TURN':
        if len(tokens) == 2 and tokens[1][0] == 'DIRECTION':
            return ASTNode('TURN', tokens[1][1].lower())
        raise SyntacticError(line_num, "Sintaxis inválida para 'turn'. Debe ser: turn <left|right>")

    # run <number>
    if t0 == 'RUN':
        if len(tokens) == 2 and tokens[1][0] == 'NUMBER':
            return ASTNode('RUN', int(tokens[1][1]))
        raise SyntacticError(line_num, "Sintaxis inválida para 'run'. Debe ser: run <number>")

    # sound <string>
    if t0 == 'SOUND':
        if len(tokens) == 2 and tokens[1][0] == 'STRING':
            return ASTNode('SOUND', tokens[1][1].strip('"'))
        raise SyntacticError(line_num, 'Sintaxis inválida para \'sound\'. Debe ser: sound "text"')

    raise SyntacticError(line_num, f"Comando desconocido '{tokens[0][1]}'")

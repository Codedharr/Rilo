# interpreter.py

from lexer import lex
from parser import parse
from robot import Robot
from errors import RiloError

class Interpreter:
    def __init__(self, filepath):
        self.filepath = filepath
        self.robot = Robot()
        self.errors = []

    def run(self):
        with open(self.filepath, encoding='utf-8') as src:
            for i, raw in enumerate(src, 1):
                line = raw.strip()
                if not line or line.startswith('#'):
                    continue
                try:
                    # 1) Léxico
                    tokens = lex(line, i)
                    print(f"Línea {i} tokens:", tokens)
                    # 2) Sintaxis
                    ast = parse(tokens, i)
                    print(f"Línea {i} AST:", ast)
                    # 3) Semántica / Ejecución
                    typ = ast.type
                    if typ == 'START':
                        self.robot.start(i)
                    elif typ == 'STOP':
                        self.robot.stop(i)
                    elif typ == 'MOVE':
                        self.robot.move(*ast.value, i)
                    elif typ == 'TURN':
                        self.robot.turn(ast.value, i)
                    elif typ == 'RUN':
                        self.robot.run(ast.value, i)
                    elif typ == 'SOUND':
                        self.robot.sound(ast.value, i)
                except RiloError as e:
                    print(">>", e)
                    self.errors.append(e)
        # Resumen de errores
        if self.errors:
            print("\n=== ERRORES DETECTADOS ===")
            for err in self.errors:
                print(err)
        else:
            print("\nNo se detectaron errores.")
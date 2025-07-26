# robot.py

import math
from errors import SemanticError

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.active = False

    def start(self, line):
        if self.active:
            raise SemanticError(line, "start(): el robot ya está iniciado")
        self.active = True
        print(">> start() -> Robot iniciado.")

    def stop(self, line):
        if not self.active:
            raise SemanticError(line, "stop(): el robot no está iniciado")
        self.active = False
        print(f">> stop() -> Robot detenido en ({self.x:.2f}, {self.y:.2f}), ángulo {self.angle}°.")

    def move(self, direction, dist, line):
        if not self.active:
            raise SemanticError(line, "move(): el robot no está iniciado")
        if dist < 0:
            raise SemanticError(line, "move(): la distancia debe ser un entero positivo")
        rad = math.radians(self.angle)
        d = dist if direction == "forward" else -dist
        self.x += d * math.sin(rad)
        self.y += d * math.cos(rad)
        print(f">> move {direction} {dist} -> Posición: ({self.x:.2f}, {self.y:.2f}), ángulo {self.angle}°.")

    def turn(self, direction, line):
        if not self.active:
            raise SemanticError(line, "turn(): el robot no está iniciado")
        if direction not in ('left','right'):
            raise SemanticError(line, f"turn(): dirección inválida '{direction}'")
        self.angle = (self.angle + (90 if direction=='right' else -90)) % 360
        print(f">> turn {direction} -> ángulo {self.angle}°.")

    def run(self, dist, line):
        # 'run' es alias de 'move forward'
        self.move("forward", dist, line)

    def sound(self, text, line):
        if not self.active:
            raise SemanticError(line, "sound(): el robot no está iniciado")
        print(f'>> sound "{text}" -> Emite sonido: {text}')



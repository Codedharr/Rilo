# robot.py

import math
from errors import SemanticError

class Robot:
    def __init__(self, visualizer=None):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.active = False
        self.vis = visualizer

    def start(self, line):
        """Enciende el robot y notifica estado inicial."""
        if self.active:
            raise SemanticError(line, "El robot ya está encendido. Usa stop() antes de volver a iniciar.")
        self.active = True
        print("[OK] 🚀 Rilo está listo. ¡Robot encendido!")
        if self.vis:
            self.vis.start()

    def stop(self, line):
        """Apaga el robot y muestra su posición final."""
        if not self.active:
            raise SemanticError(line, "No puedes detener un robot apagado. Usa start() para encenderlo primero.")
        self.active = False
        print(f"[OK] 🛑 Robot detenido en posición ({self.x:.2f}, {self.y:.2f}), orientación {self.angle}°.")
        if self.vis:
            self.vis.stop()

    def move(self, direction, dist, line):
        """Desplaza el robot hacia adelante o atrás y muestra el nuevo estado."""
        if not self.active:
            raise SemanticError(line, "Primero debes encender el robot con start() antes de moverlo.")
        if not isinstance(dist, int) or dist < 0:
            raise SemanticError(line, "La distancia debe ser un número entero positivo mayor que cero.")
        rad = math.radians(self.angle)
        delta = dist if direction == "forward" else -dist
        dx = delta * math.sin(rad)
        dy = delta * math.cos(rad)
        self.x += dx
        self.y += dy
        dir_text = "adelante" if direction == "forward" else "atrás"
        print(
            f"[OK] Rilo avanzó {dist} unidades hacia {dir_text}. "
            f"Posición actual: ({self.x:.2f}, {self.y:.2f}), mirando {self.angle}°."
        )
        if self.vis:
            # Escalamos la distancia para la visualización gráfica
            self.vis.move(delta)

    def turn(self, direction, line):
        """Gira el robot 90° a la izquierda o derecha."""
        if not self.active:
            raise SemanticError(line, "Activa el robot con start() antes de girarlo.")
        if direction not in ('left','right'):
            raise SemanticError(line, "Dirección no válida para girar. Usa 'left' o 'right'.")
        # En pantalla Turtle, girar a la derecha es girar -90° y a la izquierda +90°
        angle_delta = -90 if direction == 'right' else 90
        self.angle = (self.angle + (90 if direction == 'right' else -90)) % 360
        dir_text = "derecha" if direction == 'right' else "izquierda"
        print(f"[OK] Rilo giró hacia la {dir_text}. Nueva orientación: {self.angle}°.")
        if self.vis:
            self.vis.turn(angle_delta)

    def run(self, dist, line):
        """Alias de move forward con mensaje específico de correr."""
        if not self.active:
            raise SemanticError(line, "Debes encender el robot con start() antes de correr.")
        print(f"[OK] ¡Rilo corre {dist} unidades!")
        # Reutilizamos move para la lógica
        self.move("forward", dist, line)

    def sound(self, text, line):
        """Emite un sonido o mensaje y lo notifica en consola."""
        if not self.active:
            raise SemanticError(line, "Inicia el robot con start() antes de emitir sonidos.")
        print(f"[OK] 🔊 Rilo emite sonido: \"{text}\"")
        if self.vis:
            self.vis.sound(text)

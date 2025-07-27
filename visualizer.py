# visualizer.py

import turtle

class RiloVisualizer:
    def __init__(self):
        # Configuración de la ventana
        self.screen = turtle.Screen()
        self.screen.title("Rilo Simulator")
        self.t = turtle.Turtle()
        self.t.shape("triangle")
        self.t.color("blue")
        self.t.penup()
        self.t.speed(1)

    def start(self):
        self.t.home()
        self.t.clear()
        self.t.showturtle()

    def stop(self):
        self.t.hideturtle()

    def move(self, distance):
        # Avanza o retrocede según signo de distance
        self.t.pendown()
        self.t.forward(distance * 10)  # escalar para pantalla
        self.t.penup()

    def turn(self, angle):
        # Gira la tortuga
        self.t.left(angle)

    def sound(self, text):
        # Mostrar texto temporal
        x, y = self.t.position()
        self.screen.textinput("Rilo Sound", f"🔊 {text}")  # cuadro de diálogo

    def close(self):
        self.screen.bye()

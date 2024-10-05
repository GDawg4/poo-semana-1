from Shape import Shape
from math import pi


class Circulo(Shape):
    def __init__(self, color, radio):
        super().__init__(color)
        self._radio = radio

    def area(self):
        return pi * self._radio**2

    def dibujar(self):
        return f"Hola soy un círculo de color {self._color}"

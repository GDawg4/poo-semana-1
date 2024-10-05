from math import sqrt
from Shape import Shape


class Pentagono(Shape):
    def __init__(self, color, lado):
        super().__init__(color)
        self._lado = lado

    def area(self):
        # Fórmula para el área de un pentagono regular
        # area= 1/4 √5(5+2√5) * lado₂
        return (1 / 4) * sqrt(5 * (5 + 2 * sqrt(5))) * self._lado**2

    def dibujar(self):
        return f"Hola, soy un pentagono de color {self._color} y mi lado mide {self._lado} unidades"

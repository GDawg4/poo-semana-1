from Shape import Shape


class Cuadrado(Shape):
    def __init__(self, color, lado):
        super().__init__(color)
        self._lado = lado

    def area(self):
        self._area = self._lado**2
        return self._area

    def dibujar(self):
        return f"soy un cuadrado con color {self._color}"

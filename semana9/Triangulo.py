from Shape import Shape


class Triangulo(Shape):
    def __init__(self, color, base, altura):
        self.base = base
        self.altura = altura
        super().__init__(color)

    def area(self):
        return (self.base * self.altura) / 2

    def dibujar(self):
        return f"Hola soy un triangulo de color: {self._color} y de area: {self.area()}"

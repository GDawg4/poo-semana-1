from Shape import Shape


class Rectangulo(Shape):
    def __init__(self, base, altura, color):
        super().__init__(color)
        self._base = base
        self._altura = altura

    def area(self):
        return self._altura * self._base

    def dibujar(self):
        return f"Soy un rectángulo de color: {self._color}"

from typing import List

from Shape import Shape
from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Triangulo import Triangulo
from Pentagono import Pentagono


def obtener_area(forma: Shape):
    return forma.area()


circulo = Circulo("rojo", 3)
cuadrado = Cuadrado("verde", 8)
rectangulo = Rectangulo(5, 3, "Amarillo")
triangulo = Triangulo("verde", 4, 6)
pentagono = Pentagono("azul", 5)

formas: List[Shape] = [circulo, cuadrado, rectangulo, triangulo, pentagono]

for forma in formas:
    print(forma.dibujar())
    print(obtener_area(forma))

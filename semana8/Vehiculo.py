from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, color, marca, anio):
        self.__color = color
        self.__marca = marca
        self.__anio = anio
        self.__kilometraje = 0

    @property
    @abstractmethod
    def ruedas(self):
        pass

    @abstractmethod
    def avanzar(self, kilometros):
        pass

    def cambiar_color(self, color):
        if color in ["rojo", "blanco", "negro"]:
            self.__color = color
            print(f"Color cambiado a {color}")
        else:
            print("No se puede")
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, color, marca, anio):
        self._color = color
        self._marca = marca
        self._anio = anio
        self._kilometraje = 0

    @property
    @abstractmethod
    def ruedas(self):
        pass

    @abstractmethod
    def avanzar(self, kilometros):
        pass

    # @property
    # def marca(self):
    #     return self.__marca

    # @property
    # def anio(self):
    #     return self.__anio
    
    # @property
    # def color(self):
    #     return self.__color

    def cambiar_color(self, color):
        if color in ["rojo", "blanco", "negro"]:
            self.__color = color
            print(f"Color cambiado a {color}")
        else:
            print("No se puede")
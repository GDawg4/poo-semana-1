from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, marca, anio, tipo):
        super().__init__(color, marca, anio)
        self.__tipo = tipo
        self.__ruedas = 2
        
    def avanzar(self, kilometros = 10):
        self.__kilometraje += kilometros

    @property
    def ruedas(self):
        return self.__ruedas
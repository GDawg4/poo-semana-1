from Automotor import Automotor

class Moto(Automotor):
    def __init__(self, color, numero_serie, marca, modelo, anio):
        super().__init__(color, numero_serie, marca, modelo, anio)
        self.__ruedas = 2
    
    @property
    def ruedas(self):
        return self.__ruedas
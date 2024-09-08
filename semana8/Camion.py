from Automotor import Automotor

class Camion(Automotor):
    def __init__(self, color, numero_serie, marca, modelo, anio, claxon):
        super().__init__(color, numero_serie, marca, modelo, anio)
        self.__claxon = claxon
        self.__ruedas = 18

    @property
    def ruedas(self):
        return self.__ruedas

    def sonar_claxon(self):
        return '*beep beep*'

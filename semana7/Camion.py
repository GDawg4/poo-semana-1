from Automotor import Automotor

class Camion(Automotor):
    def __init__(self, color, numero_serie, marca, modelo, anio, claxon):
        super().__init__(color, numero_serie, marca, modelo, anio)
        self.__claxon = claxon

    def sonar_claxon(self):
        return '*beep beep*'

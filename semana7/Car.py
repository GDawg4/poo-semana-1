from Radio import Radio
from Automotor import Automotor


# Definiendo clase carro
class Carro(Automotor):
    def __init__(self, color, numero_serie, marca, modelo, anio, central, radio=None):
        super().__init__(color, numero_serie, marca, modelo, anio)
        self.central = central
        if radio is None:
            self.__radio = Radio(central)
        else:
            self.__radio = radio

    @property
    def radio(self):
        return self.__radio
    
    def get_estacion(self):
        return self.__radio.get_estacion()
    
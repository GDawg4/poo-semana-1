from Registrador import Registrador
from Car import Carro
from Moto import Moto
from Camion import Camion
from Vehiculo import Vehiculo

class RegistradorCarro(Registrador):
    def factory(self) -> Vehiculo:
        print(f'Placa tipo P')
        # Cosas de carros
        return Carro('rojo', 123, 'Patito', 'Patito1', 1997)

class RegistradorMoto(Registrador):
    def factory(self) -> Vehiculo:
        print(f'Placa tipo M')
        # Cosas de motos
        return Moto('verde', 321, 'Vaquita', 'Mooto 1', 2012)

class RegistradorCamion(Registrador):
    def factory(self) -> Vehiculo:
        print(f'Placa tipo C')
        # Cosas de camiones
        return Camion('blanco', 111, 'Hino', 'Hinojo', 2000, 'claxon')
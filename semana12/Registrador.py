from abc import abstractmethod, ABC
from Vehiculo import Vehiculo

class Registrador(ABC):
    @abstractmethod
    def factory(self) -> Vehiculo:
        pass

    def registrar(self):
        # Cosas de todos
        # M_s operaciones
        vehiculo: Vehiculo = self.factory()
        print('Operaciones adicionales')
        print(f'Vehiculo color {vehiculo._color}')
        # M_s operaciones
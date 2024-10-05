from abc import ABC, abstractmethod
from Vehiculo import Vehiculo

class Automotor(Vehiculo):
    def __init__(self, color, numero_serie, marca, modelo, anio):
        super().__init__(color, marca, anio)
        self.__numero_serie = numero_serie
        self.__modelo = modelo
        # Flotante
        self.__gasolina = 0
        self.__gasolina_max = 12
        self.__eficiencia = 32
    
    def __str__(self) -> str:
        return f"Un automotor {self._marca} {self.__modelo} {self._anio} color {self._color} con kilometraje {self._kilometraje}"
    
    def get_gasolina(self):
        return f"Este automotor tiene {self.__gasolina} galones"
    
    def get_color(self):
        return self.__color
    
    def get_numero_de_serie(self):
        return self.__numero_serie

    def agregar_gasolina(self, galones):
        if galones > 0 and self.__gasolina + galones <= self.__gasolina_max:
            self.__gasolina += galones
        else:
            print(f"Excede el l_mite")

    def avanzar(self, kilometros=10.0):
        # Km que queremos avanzar
        # Ver cu_nta gasolina tenemos
        # Ver cu_nta gasolina gastar_amos
        gasolina_total = kilometros / self.__eficiencia
        if self.__gasolina > gasolina_total:
            # self.__gasolina = self.__gasolina - gasolina_total
            self.__gasolina -= gasolina_total
            # self.__kilometraje = self.__kilometraje + kilometros
            self._kilometraje += kilometros
        elif self.__gasolina < gasolina_total:
            print("Se qued_ sin gasolina")
            # Calcular cu_nta distancia podemos avanzar
            km_alcanzados = self.__gasolina * self.__eficiencia
            # Agregar kilometros
            self._kilometraje += km_alcanzados
            # Poner gasolina en 0, porque se acab_
            self.__gasolina = 0
        else:
            self._kilometraje += kilometros
            self.__gasolina = 0
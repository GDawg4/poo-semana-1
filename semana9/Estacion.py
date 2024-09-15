class Estacion:
    def __init__(self, nombre, frecuencia, tipo):
        self.__nombre = nombre
        self.__frecuencia = frecuencia
        self.__tipo = tipo
        self.__activo = True

    def __str__(self) -> str:
        return f'Estacion {self.__nombre} en {self.__frecuencia} de tipo {self.__tipo}'
    
    def __repr__(self) -> str:
        return f'Estacion {self.__nombre} en {self.__frecuencia} de tipo {self.__tipo}'

    def suena(self):
        if self.__activo:
            if self.__tipo == 1:
                return "Última hora..."
            elif self.__tipo == 2:
                return "Tiriri"
            else:
                return "zzzzzzz"

    def activo(self):
        return self.__activo

    def get_frecuencia(self):
        return self.__frecuencia
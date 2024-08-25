class Radio:
    def __init__(self, central):
        self.__volumen = 0
        self.__estaci_n = 0.0
        self.__encendido = False
        self.__pm = True
        self.__central = central

    def subir_volumen(self):
        self.__volumen += 1

    def bajar_volumen(self):
        self.__volumen -= 1

    def encender(self):
        self.__encendido = True

    def apagar(self):
        self.__encendido = False

    # Manual
    def subir_estacion(self):
        self.__estaci_n += 0.1

    # Manual
    def bajar_estacion(self):
        self.__estaci_n -= 0.1

    def escanear(self):
        estaciones_disponibles = self.__central.buscar_estaciones_activas()
        mas_altas = [
            estacion.get_frecuencia()
            for estacion in estaciones_disponibles
            if estacion.get_frecuencia() > self.__estaci_n
        ]
        # if len(mas_altas) > 0
        if mas_altas:
            self.__estaci_n = mas_altas[0]
        else:
            self.__estaci_n = estaciones_disponibles[0].get_frecuencia()

        return True

    def __str__(self) -> str:
        return f'Radio en estacion {self.__estaci_n}'

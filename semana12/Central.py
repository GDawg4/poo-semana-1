class Central:
    def __init__(self, estaciones) -> None:
        self.__estaciones = estaciones  # [estacion1, estacion2, estacion3]

    def buscar_estaciones_activas(self):
        estaciones_activas = []
        for estacion in self.__estaciones:
            if estacion.activo():
                estaciones_activas.append(estacion)
        return sorted(
            estaciones_activas, key=lambda estacion: estacion.get_frecuencia()
        )
    
    def agregar_estacion(self, estacion):
        self.__estaciones.append(estacion)
        

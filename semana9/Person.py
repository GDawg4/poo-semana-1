class Persona:
    def __init__(self, nombre, apellido, anio_de_nacimiento, automotor=None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__anio_de_nacimiento = anio_de_nacimiento
        self.__automotores = {}
        if automotor:
            self.agregar_automotor(automotor)

    def __str__(self):
        descripcion = f"Una persona de nombre {self.__nombre} {self.__apellido} "
        if self.__automotores:
            return descripcion + f"con automotor {self.__automotores.get_color()}"
        else:
            return descripcion + "sin automotor"

    def agregar_automotor(self, automotor):
        if 2024 - self.__anio_de_nacimiento > 16:
            self.__automotores[automotor.get_numero_de_serie()] = automotor
            print("Automotor agregado")
        else:
            print("No puede tener automotor")

    def get_nombre(self):
        # Medir cuántas veces se accede al nombre
        # veces += 1
        return self.__nombre

    def set_nombre(self, nombre):
        # Revisar que no sea un número
        # Revisar que no sea el mismo
        # Revisar que no sea broma
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    # ...

    def get_nombre_completo(self):
        return f"Nombre completo: {self.__nombre} {self.__apellido}"

    def manejar(self):
        if self.__automotores:
            self.__automotores.avanzar()

    def get_estacion_actual(self):
        if hasattr(self.__automotores, 'radio'):
            return f'Escuchando {self.__automotores.get_estacion()}'
        else:
            return f'No hay radio'
        
    def get_automotores(self):
        return list(self.__automotores)
    
    def get_automotor(self, numero_de_serie):
        if numero_de_serie in self.__automotores:
            return self.__automotores[numero_de_serie]
        return 0
    
    def manejar_automotor(self, numero_de_serie, kilometros):
        automotor = self.get_automotor(numero_de_serie)
        if automotor:
            automotor.avanzar(kilometros)
        return
    
    def agregar_gasolina_automotor(self, numero_de_serie, galones):
        automotor = self.get_automotor(numero_de_serie)
        if automotor:
            automotor.agregar_gasolina(galones)
        return
    
    def agregar_gasolina_automotores(self, galones):
        for key, value in self.__automotores.items():
            print(f'Agregando gasolina a {key}')
            value.agregar_gasolina(galones)

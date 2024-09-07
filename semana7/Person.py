class Persona:
    def __init__(self, nombre, apellido, anio_de_nacimiento, automotor=None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__anio_de_nacimiento = anio_de_nacimiento
        self.__automotor = None
        if automotor:
            self.agregar_automotor(automotor)

    def __str__(self):
        descripcion = f"Una persona de nombre {self.__nombre} {self.__apellido} "
        if self.__automotor:
            return descripcion + f"con automotor {self.__automotor.get_color()}"
        else:
            return descripcion + "sin automotor"

    def agregar_automotor(self, automotor):
        if 2024 - self.__anio_de_nacimiento > 16:
            self.__automotor = automotor
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
        if self.__automotor:
            self.__automotor.avanzar()

    def get_estacion_actual(self):
        if hasattr(self.__automotor, 'radio'):
            return f'Escuchando {self.__automotor.get_estacion()}'
        else:
            return f'No hay radio'
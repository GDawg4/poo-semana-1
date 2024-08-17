class Persona:
    def __init__(self, nombre, apellido, anio_de_nacimiento, carro=None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__anio_de_nacimiento = anio_de_nacimiento
        self.__carro = None
        self.agregar_carro(carro)

    def __str__(self):
        descripcion = f"Una persona de nombre {self.__nombre} {self.__apellido} "
        if self.__carro:
            return descripcion + f"con carro {self.__carro.get_color()}"
        else:
            return descripcion + "sin carro"

    def agregar_carro(self, carro):
        if 2024 - self.__anio_de_nacimiento > 16:
            self.__carro = carro
            print("Carro agregado")
        else:
            print("No puede tener carro")

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
        if self.__carro:
            self.__carro.avanzar()
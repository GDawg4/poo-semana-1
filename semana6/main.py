from Car import Carro
from Person import Persona
from Central import Central
from Estacion import Estacion
from Radio import Radio

estaciones = [
    {"nombre": "Patito", "frecuencia": 102.1, "tipo": 1},
    {"nombre": "Regueton", "frecuencia": 88.9, "tipo": 2},
    {"nombre": "Rock", "frecuencia": 98.9, "tipo": 2},
    {"nombre": "Pop", "frecuencia": 95.6, "tipo": 2},
    {"nombre": "Noticias de Regueton", "frecuencia": 100.0, "tipo": 1},
]

estaciones_objeto = []

for estacion in estaciones:
    nueva_estacion = Estacion(
        estacion["nombre"], estacion["frecuencia"], estacion["tipo"]
    )
    estaciones_objeto.append(nueva_estacion)

central = Central(estaciones_objeto)
radio = Radio(central)

#carro_rojo = Carro("rojo", 123, "Honda", "Civic", 2015, central)
#carro_negro = Carro("negro", 321, "Toyota", "Yaris", 2007, central)
#juanito = Persona("Juanito", "Juanitez", 2012)
#juanita = Persona("Juanita", "Juanitez", 2006, carro_rojo)

print(radio)
radio.escanear()
print(radio)
radio.escanear()
print(radio)
radio.escanear()
print(radio)

central.agregar_estacion(Estacion('La nueva ola', 99.9, 1))

radio.escanear()
print(radio)
radio.escanear()
print(radio)
radio.escanear()
print(radio)
radio.escanear()
print(radio)
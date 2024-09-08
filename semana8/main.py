from Car import Carro
from Person import Persona
from Central import Central
from Estacion import Estacion
from Radio import Radio
from Moto import Moto
from Camion import Camion
from Bicicleta import Bicicleta
from Vehiculo import Vehiculo
from Automotor import Automotor

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

#carro_rojo = Carro('rojo', 123, 'Patito', 'Patito1', 1997, Central)
moto_verde = Moto('verde', 321, 'Vaquita', 'Mooto 1', 2012)
# #camion_blanco = Camion('blanco', 111, 'Hino', 'Hinojo', 2000, 'claxon')
# juanita = Persona('Juanita', 'Juanitez', 1990)

# bici_negra = Bicicleta('negro', 'Fuji', '2024', 'montania')
# bici_negra.cambiar_color('rojo')

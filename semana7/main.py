from Car import Carro
from Person import Persona
from Central import Central
from Estacion import Estacion
from Radio import Radio
from Moto import Moto
from Camion import Camion

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
#carro_rojo.agregar_gasolina(10)
#print(carro_rojo.get_estacion())
# print(carro_rojo.get_gasolina())
# carro_rojo.avanzar()
# print(carro_rojo.get_gasolina())

#moto_verde = Moto('verde', 321, 'Vaquita', 'Mooto 1', 2012)
#moto_verde.agregar_gasolina(10)
# print(moto_verde.get_gasolina())
# moto_verde.avanzar()
# print(moto_verde.get_gasolina())

camion_blanco = Camion('blanco', 111, 'Hino', 'Hinojo', 2000, 'claxon')
camion_blanco.agregar_gasolina(10)

juanita = Persona('Juanita', 'Juanitez', 1990)
juanita.agregar_automotor(camion_blanco)
print(juanita)
print(juanita.manejar())
# juanita.manejar()
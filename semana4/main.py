from Car import Carro
from Person import Persona

carro_rojo = Carro("rojo", 123, "Honda", "Civic", 2015)
carro_negro = Carro("negro", 321, "Toyota", "Yaris", 2007)
juanito = Persona("Juanito", "Juanitez", 2012)
juanita = Persona("Juanita", "Juanitez", 2006, carro_rojo)

print(juanita)
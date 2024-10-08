# pasajero.py

from boleto import Boleto

class Pasajero:
    def __init__(self, nombre, edad, genero, boleto: Boleto):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.boleto = boleto





# boleto.py

class Boleto:
    def __init__(self, vagon, silla, tipo):
        self.vagon = vagon
        self.silla = silla
        self.tipo = tipo
        self.precio = self.calcular_precio()

    def calcular_precio(self):
        if self.tipo == 'A':
            return 2000
        elif self.tipo == 'B':
            return 4000
        elif self.tipo == 'C':
            return 6000
        return 0
# tren.py

from pasajero import Pasajero

class Tren:
    def __init__(self, num_vagones):
        self.num_vagones = num_vagones
        self.sillas = {f"{vagon}-{silla:02}": None for vagon in range(1, num_vagones+1) for silla in range(1, 11)}
        self.paradas = 0
        self.subidas = 0
        self.bajadas = 0

    def subir_pasajero(self, pasajero: Pasajero):
        silla = f"{pasajero.boleto.vagon}-{pasajero.boleto.silla:02}"
        if self.sillas[silla] is not None:
            print(f"Silla {silla} está ocupada.")
        else:
            self.sillas[silla] = pasajero
            self.subidas += 1
            self.paradas += 1
            print(f"Pasajero {pasajero.nombre} se ha subido al tren en la silla {silla}.")

    def bajar_pasajero(self, vagon, silla):
        silla_id = f"{vagon}-{silla:02}"
        if self.sillas[silla_id] is None:
            print(f"No hay pasajero en la silla {silla_id}.")
        else:
            pasajero = self.sillas[silla_id]
            self.sillas[silla_id] = None
            self.bajadas += 1
            self.paradas += 1
            print(f"Pasajero {pasajero.nombre} se ha bajado del tren de la silla {silla_id}.")

    def listar_pasajeros(self):
        print("\nLista de pasajeros:")
        for silla, pasajero in self.sillas.items():
            if pasajero is not None:
                print(f"Silla {silla}: {pasajero.nombre}, {pasajero.edad} años, {pasajero.genero}")
        print()

    def contar_pasajeros_por_genero(self):
        conteo = {"masculino": 0, "femenino": 0, "otro": 0}
        for pasajero in self.sillas.values():
            if pasajero is not None:
                conteo[pasajero.genero.lower()] += 1
        print(f"Masculinos: {conteo['masculino']}, Femeninos: {conteo['femenino']}, Otro: {conteo['otro']}")

    def ordenar_pasajeros_por_edad(self):
        pasajeros = [pasajero for pasajero in self.sillas.values() if pasajero is not None]
        pasajeros_ordenados = sorted(pasajeros, key=lambda p: p.edad)
        print("\nPasajeros ordenados por edad:")
        for pasajero in pasajeros_ordenados:
            silla = f"{pasajero.boleto.vagon}-{pasajero.boleto.silla:02}"
            print(f"Silla {silla}: {pasajero.nombre}, {pasajero.edad} años")
        print()

    def calcular_total_pagado(self):
        total = {"A": 0, "B": 0, "C": 0}
        for pasajero in self.sillas.values():
            if pasajero is not None:
                total[pasajero.boleto.tipo] += pasajero.boleto.precio
        print(f"Total pagado - Tipo A: {total['A']} | Tipo B: {total['B']} | Tipo C: {total['C']}")

    def mostrar_total_subidas_bajadas(self):
        print(f"Total de personas subidas: {self.subidas}, Total de personas bajadas: {self.bajadas}")

    def buscar_pasajero(self, nombre):
        print(f"Buscando pasajero(s) con el nombre '{nombre}':")
        encontrado = False
        for silla, pasajero in self.sillas.items():
            if pasajero is not None and pasajero.nombre.lower() == nombre.lower():
                print(f"Pasajero encontrado en silla {silla}: {pasajero.nombre}, {pasajero.edad} años")
                encontrado = True
        if not encontrado:
            print("No se encontraron pasajeros con ese nombre.")
        print()

# main.py

from tren import Tren
from pasajero import Pasajero
from boleto import Boleto

# Menú interactivo
def menu():
    num_vagones = int(input("Ingrese el número de vagones del tren: "))
    tren = Tren(num_vagones)

    while True:
        print("\n--- Menú del sistema de gestión del tren ---")
        print("1. Subir Pasajero")
        print("2. Bajar Pasajero")
        print("3. Listar Pasajeros")
        print("4. Contar Pasajeros por Género")
        print("5. Ordenar Pasajeros por Edad")
        print("6. Calcular Total Pagado por Boletos")
        print("7. Mostrar número total de Personas Subidas y de Personas Bajadas")
        print("8. Buscar un Pasajero")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del pasajero: ")
            edad = int(input("Edad del pasajero: "))
            genero = input("Género del pasajero (masculino, femenino, otro): ")
            vagon = int(input("Número de vagón: "))
            silla = int(input("Número de silla: "))
            tipo = input("Tipo de boleto (A, B, C): ")

            boleto = Boleto(vagon, silla, tipo)
            pasajero = Pasajero(nombre, edad, genero, boleto)
            tren.subir_pasajero(pasajero)

        elif opcion == "2":
            vagon = int(input("Número de vagón: "))
            silla = int(input("Número de silla: "))
            tren.bajar_pasajero(vagon, silla)

        elif opcion == "3":
            tren.listar_pasajeros()

        elif opcion == "4":
            tren.contar_pasajeros_por_genero()

        elif opcion == "5":
            tren.ordenar_pasajeros_por_edad()

        elif opcion == "6":
            tren.calcular_total_pagado()

        elif opcion == "7":
            tren.mostrar_total_subidas_bajadas()

        elif opcion == "8":
            nombre = input("Ingrese el nombre del pasajero a buscar: ")
            tren.buscar_pasajero(nombre)

        elif opcion == "9":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    menu()

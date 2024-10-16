from tren import Tren
from boleto import Boleto
from pasajero import Pasajero

def subir_pasajero(tren):
    nombre = input("Nombre del pasajero: ")
    edad = int(input("Edad del pasajero: "))
    genero = input("Género del pasajero (masculino, femenino, otro): ")
    vagon = int(input("Número de vagón: "))
    silla = int(input("Número de silla: "))
    tipo = input("Tipo de boleto (A, B, C): ")

    boleto = Boleto(vagon, silla, tipo)
    pasajero = Pasajero(nombre, edad, genero, boleto)
    tren.subir_pasajero(pasajero)
    
def bajar_pasajero(tren):
    vagon = int(input("Número de vagón: "))
    silla = int(input("Número de silla: "))
    tren.bajar_pasajero(vagon, silla)

def listar_pasajeros(tren):
    tren.listar_pasajeros()

def contar_pasajeros_genero(tren):
    tren.contar_pasajeros_por_genero()

def ordenar_pasajeros_edad(tren):
    tren.ordenar_pasajeros_por_edad()

def calcular_total_pagado(tren):
    tren.calcular_total_pagado()

def mostrar_total_subidas_bajadas(tren):
    tren.mostrar_total_subidas_bajadas()

def buscar_pasajero(tren):
    nombre = input("Ingrese el nombre del pasajero a buscar: ")
    tren.buscar_pasajero(nombre)
    



def mostrar_menu():
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
#opciones

aciones = {
    1: subir_pasajero,
    2: bajar_pasajero,
    3: listar_pasajeros,
    4: contar_pasajeros_genero,
    5: ordenar_pasajeros_edad,
    6: calcular_total_pagado,
    7: mostrar_total_subidas_bajadas,
    8: buscar_pasajero
}

#menu interactivo

def ejecutar_tren():
    num_vagones = int(input("Ingrese el número de vagones del tren: "))
    tren = Tren(num_vagones)
    
    while True:
        mostrar_menu()
        opcion = int(input("Seleciona una opcion: "))
        if opcion == 9:
            break
        accion = aciones.get(opcion)
        accion(tren)

if __name__ == "__main__":
    ejecutar_tren()

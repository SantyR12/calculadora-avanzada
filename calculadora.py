import math

def menu():
    print("\n===== CALCULADORA AVANZADA =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Porcentaje")
    print("7. Raíz cuadrada")
    print("8. Conversión de temperatura (C ↔ F)")
    print("9. Salir")

def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b): return "Error: división por cero" if b == 0 else a / b
def potencia(a, b): return a ** b
def porcentaje(a, b): return (a * b) / 100
def raiz_cuadrada(a): return "Error: número negativo" if a < 0 else math.sqrt(a)

def convertir_temp(valor, unidad_origen, unidad_destino):
    if unidad_origen == unidad_destino:
        return "Error: las unidades son iguales"
    elif unidad_origen == "C" and unidad_destino == "F":
        return (valor * 9/5) + 32
    elif unidad_origen == "F" and unidad_destino == "C":
        return (valor - 32) * 5/9
    else:
        return "Error: unidades inválidas"

while True:
    menu()
    opcion = input("Selecciona una opción (1-9): ")

    if opcion == "9":
        print("Saliendo de la calculadora...")
        break

    if opcion in ["1", "2", "3", "4", "5", "6"]:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        if opcion == "1": print("Resultado:", suma(a, b))
        elif opcion == "2": print("Resultado:", resta(a, b))
        elif opcion == "3": print("Resultado:", multiplicacion(a, b))
        elif opcion == "4": print("Resultado:", division(a, b))
        elif opcion == "5": print("Resultado:", potencia(a, b))
        elif opcion == "6": print("Resultado:", porcentaje(a, b))
    elif opcion == "7":
        a = float(input("Ingresa un número: "))
        print("Resultado:", raiz_cuadrada(a))
    elif opcion == "8":
        valor = float(input("Ingresa el valor: "))
        unidad_origen = input("Unidad de origen (C/F): ").upper()
        unidad_destino = input("Unidad destino (C/F): ").upper()
        print("Resultado:", convertir_temp(valor, unidad_origen, unidad_destino))
    else:
        print("Opción no válida.")

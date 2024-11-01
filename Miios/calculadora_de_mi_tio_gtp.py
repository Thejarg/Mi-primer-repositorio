# Funciones para las operaciones básicas
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: No se puede dividir entre 0."
    return x / y

# Función principal de la calculadora
def calculadora():
    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    # Recoger la elección del usuario
    eleccion = input("Introduce tu opción (1/2/3/4): ")

    if eleccion in ['1', '2', '3', '4']:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if eleccion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")

        elif eleccion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")

        elif eleccion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

        elif eleccion == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

# Ejecutar la calculadora
calculadora()

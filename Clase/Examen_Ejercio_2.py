
"""

   Problema 2. Sistema de gestión de productos de una tienda

    Eres el encargado de crear un sistema básico para administrar 
    productos de una tienda. Este sistema debe permitir:

        - Registrar productos con su nombre y precio.
        - Consultar productos con precios específicos.
        - Actualizar los precios de productos existentes.
        - Obtener un resumen de todos los productos con ciertos filtros.

        Requerimientos
        
        Registro de productos:
            - Crea una lista vacía llamada productos.
            - Cada producto debe ser un diccionario con las claves: 
                "nombre" (cadena de texto) y "precio" (flotante).
            - Usa un bucle while para permitir al usuario agregar productos 
                hasta que decida detenerse.
        
        Consulta de productos por precio:
            - Pide al usuario que ingrese un precio límite.
            - Usa una list comprehension para generar una lista de productos 
                cuyo precio sea menor o igual al precio límite dado.
            - Muestra la lista resultante o indica que no hay productos en ese
                rango de precio.

        Actualización de precios:

            - Solicita al usuario el nombre del producto que quiere
                actualizar.
            - Si el producto existe, pide el nuevo precio y actualiza
                su valor.
            - Usa una estructura if para verificar si el producto 
                existe; si no, muestra un mensaje indicando que no se encontró.

        Resumen de productos:

            - Utiliza un bucle for para mostrar un resumen de todos los 
                productos registrados en un formato claro.
            - Si el usuario quiere filtrar los productos con precio mayor
                a un valor dado, filtra la lista y muestra solo los productos
                que cumplan con el criterio. 

"""
from colorama import init, Fore, Style
init(autoreset=True)

productos = []

# Registro de productos
while True:
    nombre = input("Ingresa el nombre del producto (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    precio = float(input("Ingresa el precio del producto: "))
    productos.append({"nombre": nombre, "precio": precio})

# Consulta de productos por precio
precio_limite = float(input("Ingresa un precio límite para consultar productos: "))
productos_filtrados = [p for p in productos if p["precio"] <= precio_limite]
if productos_filtrados:
    print(Fore.GREEN + "Productos con precio menor o igual a", precio_limite, ":")
    for p in productos_filtrados:
        print(Fore.YELLOW + f"Nombre: {p['nombre']}, Precio: {p['precio']}")
else:
    print(Fore.RED + "No hay productos en ese rango de precio.")

# Actualización de precios
nombre_actualizar = input("Ingresa el nombre del producto que quieres actualizar: ")
encontrado = False
for p in productos:
    if p["nombre"].lower() == nombre_actualizar.lower():
        nuevo_precio = float(input("Ingresa el nuevo precio: "))
        p["precio"] = nuevo_precio
        encontrado = True
        print(Fore.GREEN + "Precio actualizado.")
        break
if not encontrado:
    print(Fore.RED + "Producto no encontrado.")

# Resumen de productos
print(Style.RESET_ALL + "Resumen de todos los productos:")
for p in productos:
    print(Fore.BLUE + f"Nombre: {p['nombre']}, Precio: {p['precio']}")

# Filtrar productos por precio mayor a un valor dado
precio_filtro = float(input("Ingresa un precio para filtrar productos con precio mayor a este valor: "))
productos_filtrados = [p for p in productos if p["precio"] > precio_filtro]
if productos_filtrados:
    print(Fore.GREEN + "Productos con precio mayor a", precio_filtro, ":")
    for p in productos_filtrados:
        print(Fore.YELLOW + f"Nombre: {p['nombre']}, Precio: {p['precio']}")
else:
    print(Fore.RED + "No hay productos en ese rango de precio.")

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

Productito = []
while True:
    PE = (Fore.LIGHTCYAN_EX+"Porfavor ingresa el nombre del producto"+Style.RESET_ALL+Fore.LIGHTRED_EX+"(o escribe salir para terminar): "+Style.RESET_ALL)
    Producto = input(PE)
    if Producto.lower() == 'salir' or Producto.lower() == 'exit':
        break
    prechio = (Fore.LIGHTCYAN_EX+"Ahora dime cuanto quieres que cueste: "+Style.RESET_ALL)
    precio = float(input(prechio))
    El_append = ({'Producto': Producto,'Precio': precio})
    Productito.append(El_append)
    print(f"Agregaste {Producto} Con el precio de ${precio}")
"""
        Consulta de productos por precio:
            - Pide al usuario que ingrese un precio límite.
            - Usa una list comprehension para generar una lista de productos 
                cuyo precio sea menor o igual al precio límite dado.
            - Muestra la lista resultante o indica que no hay productos en ese
                rango de precio.

"""
while True:
    conchulta = (Fore.LIGHTCYAN_EX+"¿Deseas Consultar algun producto?"+Style.RESET_ALL+Fore.LIGHTMAGENTA_EX+"Escribe 'S' / 'N' "+Style.RESET_ALL)
    Consulta = input(conchulta)
    if Consulta.lower() == "s":
        limite = (Fore.LIGHTCYAN_EX+"Ingresa el precio maximo de consulta: ")
        que_consultas = float(input(limite))
        el_que_esta_dentro_del_rango = [con for con in Productito if con['precio']<=limite]
        if el_que_esta_dentro_del_rango:
            print(Fore.LIGHTCYAN_EX+"Precio menor o igual al limite")
            for con in el_que_esta_dentro_del_rango:
                print() 
    if Consulta.lower() == "n":
        break
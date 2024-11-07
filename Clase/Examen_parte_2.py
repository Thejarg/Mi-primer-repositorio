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
    PE = (Fore.LIGHTCYAN_EX+"Porfavor ingresa el nombre del producto"+Style.RESET_ALL+Fore.LIGHTRED_EX+" (o escribe salir para terminar): "+Style.RESET_ALL)
    Producto = input(PE)
    if Producto.lower() == 'salir' or Producto.lower() == 'exit':
        break
    prechio = (Fore.LIGHTCYAN_EX+"Ahora dime cuanto quieres que cueste: "+Style.RESET_ALL)
    precio = float(input(prechio))
    El_append = ({'Producto': Producto,'Precio': precio})
    Productito.append(El_append)
    print(f"Agregaste {Producto} Con el precio de ${precio}")

while True:
    conchulta = (Fore.LIGHTCYAN_EX+"¿Deseas Consultar algun producto?"+Style.RESET_ALL+Fore.LIGHTMAGENTA_EX+" (s/n) "+Style.RESET_ALL)
    nombre = input(conchulta)
    if nombre.lower() == "s":
        limite = (Fore.LIGHTCYAN_EX+"Ingresa el precio maximo de consulta: "+Style.RESET_ALL)
        precio = float(input(limite))
        el_que_esta_dentro_del_rango = [con for con in Productito if (con['Precio']) <= precio]
        if el_que_esta_dentro_del_rango: 
            print(Fore.LIGHTCYAN_EX + "Precio menor o igual al limite")
            for con in el_que_esta_dentro_del_rango:
                print(f"- {con['Producto']} Precio: ${str(con['Precio'])}")
        else:
            print(Fore.LIGHTRED_EX + "No hay productos con ese precio")
    elif nombre.lower() == "n":
        break

while True:
    conchulta = (Fore.LIGHTCYAN_EX+"¿Deseas  Actualizar el precio de algun producto?"+Style.RESET_ALL+Fore.LIGHTMAGENTA_EX+" (s/n) "+Style.RESET_ALL)
    nombre = input(conchulta)
    if nombre.lower() == "s":
        nombre_producto = input(Fore.LIGHTCYAN_EX+"Ingrese el nombre del producto que desea actualizar: "+Style.RESET_ALL)
        for producto in Productito:
            if producto["Producto"].lower() == nombre_producto.lower():
                nuevo_precio = float(input(Fore.GREEN+"Ingrese el nuevo precio: "+Style.RESET_ALL))
                producto["Precio"] = nuevo_precio
                print(f"Precio de '{nombre_producto}' actualizado a ${nuevo_precio}.")
                break
        else:
            print(Fore.RED+"No existe ese producto.")
    elif nombre.lower() == "n":
        break
    else:
        print(Fore.LIGHTRED_EX + "Por favor, escribe 'S' para sí o 'N' para no.")

while True:
    filtro = input(Fore.LIGHTCYAN_EX + "¿Desea ver productos con precio mayor a un valor específico?"+Style.RESET_ALL+Fore.LIGHTMAGENTA_EX+"(s/n):"+Style.RESET_ALL)

    if filtro.lower() == 's':
        minimo = float(input(Fore.YELLOW + "Ingrese el precio mínimo: "+Style.RESET_ALL))
        fil = [cto for cto in Productito if cto["Precio"] >= minimo]
        if fil:
            print(Fore.GREEN + "Productos con precio mayor al valor especificado: "+Style.RESET_ALL)
            for cto in fil:
                print(Fore.GREEN + f"{cto['Producto']}:"+Style.RESET_ALL+ f"${cto['Precio']}")
        else:
            print(Fore.RED + "No hay productos en ese rango de precio.")
    elif filtro.lower() == 'n':
        print(Fore.GREEN + "Acabamos....")
        break
    else:
        print(Fore.LIGHTRED_EX + "Por favor, escribe 'S' para sí o 'N' para no.")
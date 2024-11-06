# Lista vacía para almacenar los productos
productos = []

# Registro de productos
while True:
    print("\n--- Registro de productos ---")
    nombre = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    precio = float(input("Ingrese el precio del producto: "))
    productos.append({"nombre": nombre, "precio": precio})
    print(f"Producto '{nombre}' registrado con éxito.")

# Consulta de productos por precio
print("\n--- Consulta de productos por precio ---")
precio_limite = float(input("Ingrese el precio límite para consulta: "))
productos_en_rango = [producto for producto in productos if producto["precio"] <= precio_limite]

if productos_en_rango:
    print("Productos con precio menor o igual al límite:")
    for producto in productos_en_rango:
        print(f"- {producto['nombre']}: ${producto['precio']}")
else:
    print("No hay productos en ese rango de precio.")

# Actualización de precios
print("\n--- Actualización de precios ---")
nombre_producto = input("Ingrese el nombre del producto que desea actualizar: ")
producto_encontrado = False
for producto in productos:
    if producto["nombre"].lower() == nombre_producto.lower():
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        producto["precio"] = nuevo_precio
        print(f"Precio de '{nombre_producto}' actualizado a ${nuevo_precio}.")
        producto_encontrado = True
        break
if not producto_encontrado:
    print("Producto no encontrado.")

# Resumen de productos
print("\n--- Resumen de productos ---")
filtro = input("¿Desea ver productos con precio mayor a un valor específico? (s/n): ").lower()
if filtro == 's':
    precio_minimo = float(input("Ingrese el precio mínimo: "))
    productos_filtrados = [producto for producto in productos if producto["precio"] > precio_minimo]
    if productos_filtrados:
        print("Productos con precio mayor al valor especificado:")
        for producto in productos_filtrados:
            print(f"- {producto['nombre']}: ${producto['precio']}")
    else:
        print("No hay productos en ese rango de precio.")
else:
    print("Resumen de todos los productos:")
    for producto in productos:
        print(f"- {producto['nombre']}: ${producto['precio']}")

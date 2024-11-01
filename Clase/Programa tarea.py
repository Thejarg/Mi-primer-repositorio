"""
EJERCICIO

  1. Guardar el nombre de una persona en una variable e imprimir un mensaje de bienvenida a esa persona,
  ejemplo. "¿Hola charly, te gustaria aprender algo mas sobre python?

  2.Guarda el nombre de una persona en una varible e imprime su nombre en minusculas, mayusculas, con el formato Title.

  3. Encuentra una cita de alguna persona famosa, puede ser a la persona que admiren. Imprime la cita y el nombre del autor. por ejemplo
  'Charly mercury una vez dijo: "no lleguen tarde a clase"'

  4. Repite el ejercicio anterior, pero ahora almacena el nombre de la persona cen una variable. Despues crea un mensaje que contega la cita y
  el nombre de la persona famosa, finalmente, imprime el mensaje.

  5. Guarda el nommbre de una persona en una variable, agrega espacios, tabuladores,
  saltos de linea. imprime el nombre, despues el nombre varias veces utilizando los metodos lstrip, rstrip, strip.

  """
print("------------------------ Actividad 1 ------------------------")
name = "Josue alberto"
Saludo = f"¿Hola {name.title()}, te gustaria aprender algo mas sobre python?"
print(Saludo)

print("------------------------ Actividad 2 ------------------------")
print(name)
print(name.lower())
print(name.upper())
print(name.title())
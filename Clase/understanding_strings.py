"""
Un string es de manera sencilla una serie de caracteres.
En python todo lo que se encuentre dentro de las 
comillas simples '' o de las dobles comillas "" es 
considerado un string.

    " Esto es un string"
    ' Esto también es un string'
    
    'Le dije a un amigo, "¡Python es mi lenguage favorito!"'
    
    "El lenguage 'Python' lleva el nombre por Monty Python, no por la serpiente"

"""
print("-------------------")
print("Método title")
name = "clase de programación"
print(name)
print(name.title())
print("-------------------")
"""
    Todos los métodos van seguidos de paréntesis
    porque en ocasiones necesitan información adicional
    para funcionar, lo cuál iría dentro de los paréntesis.
    En esta ocasión, el método .title() no requiere información
    adicional.
"""
print("-------------------------")
name_of_class = "Metodología de la Programación"
print(name_of_class.title()) #Pone las primeras letras de cada texto en mayusculas
print(name_of_class.lower()) #Pone todo en minusculas 
print(name_of_class.upper()) #Pone todo en mayusculas
print(name_of_class)

"""
concatenacion o combinacion de strings
"""
firt_name = "JOSUE ALBERTO"
last_name = "REQUENA GRIMALDO"
Full_name = firt_name + " " + last_name


print(firt_name)
print(last_name)
print(Full_name.title())

print("Hi," , Full_name.title() ,"!")
mensaje = "Hi," + " " + Full_name.title() + " " + "!"
print(mensaje)
"""
Whitespace - se refiere a cualquier caracter que no se imprime,
es decir, un espacio, tabulares y finales de linea.
Los whitespaces se utilizan comunmente para organizar las salidas,
de tal manera que sea mas amigable de leer o de ver para los usuarios
"""

message3 = "\tpython python\n Java"
print(message3)
###########################################
# DIA 07/10/2024
print("------------------------------------------------------")
print("----------------Actividad 07/10/2024------------------")
# METODO RSTRIP

men = " python es mi lenguaje favorito "
print(men)
print(men.lstrip())
print(men.rstrip())
print(men.strip())

men = 'una fortaleza de "python" es su comunidad'
print(men)


"""
EJERCICIO

  1. Guardar el nombre de una persona en una variable e imprimir un mensaje de bienvenida a esa persona,
  ejemplo. "¿Hola charly, te gustaria aprender algo mas sobre python?

  2.Guarda el nombre de una persona en una varible e imprime su nombre en minusculas, mayusculas, con el formato Title.

  3. Encuentra una cita de alguna persona famosa, puede ser a la persona que admiren. Imprime la cita y el nombre del autor. por ejemplo
  'Charly mercury una vez dijo: "n lleguen tarde a clase"'

  4. Repite el ejercicio anterior, pero ahora almacena el nombre de la persona cen una variable. Despues crea un mensaje que contega la cita y
  el nombre de la persona famosa, finalmente, imprime el mensaje.

  5. Guarda el nommbre de una persona en una variable, agrega espacios, tabuladores,
  saltos de linea. imprime el nombre, despues el nombre varias veces utilizando los metodos lstrip, rstrip, strip.

  """
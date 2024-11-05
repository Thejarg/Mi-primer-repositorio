from colorama import Fore, Style

# Inicializar Colorama
import colorama
import pyfiglet
colorama.init()
"""
Problema 1 tipo entrevista 
Descifra el mensaje oculto en el siguiente texto:
se tiene las siguiente lista:
mensaje= ["u","n","e","m","i"," ","t","o"," ","Q","o","a","d","A","R"]
crea un programa ue reemplace:
   - Las letra a/A por la e
   - Las letra e/E por la i
   - Las letra i/I por la o
   - Las letra o/O por la u
   - Las letra u/U por la a
   - Las letra q/Q por la p
   - Las letra r/R por la s

muestra al final el mensaje oculto en consola con la funcion print.
(imprime el mensaje con un ciclo for para la salida, utiliza el argumento end="" para que no imprima un salto de linea en cada print)
   ejemplo:
       print(letter, end="")

"""
mensaje= ["u","n","e","m","i"," ","t","o"," ","Q","o","a","d","A","R"]
for letra in mensaje:
    if letra == "a":
        print("e", end="")
    elif letra == "A":
        print("e", end="")
    elif letra == "e":
        print("i", end="")
    elif letra == "E":
        print("i",end="")
    elif letra == "i":
        print("o", end="")
    elif letra == "I":
        print("o", end="")    
    elif letra == "o":
        print("u", end="")
    elif letra == "O":
        print("u", end="")
    elif letra == "u":
        print("a", end="")
    elif letra == "U":
        print("a", end="")    
    elif letra == "q":
        print("p", end="")
    elif letra == "Q":
        print("p", end="")    
    elif letra == "r":
        print("s", end="")
    elif letra == "R":
        print("s", end="")    
    
    else:
        print(letra, end="")

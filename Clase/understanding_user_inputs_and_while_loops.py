""""
user inputs
"""
import time
from colorama import Fore, Style
import colorama
colorama.init()
"""
print(Fore.LIGHTCYAN_EX+"----------Ingresa tu nombre---------".title()+Style.RESET_ALL)
## prompt == Instrucciones para el usuario
F = input(Fore.LIGHTYELLOW_EX+"Ingresa tu nombre: "+Style.RESET_ALL)
print(F.title() +Fore.LIGHTCYAN_EX +  ", Muy hermoso nombre"+Style.RESET_ALL)
print(type(F))
print(Fore.LIGHTCYAN_EX+"----------Ingresa tu edad---------".title()+Style.RESET_ALL)
#prompt para pedir un numero
prompt = (Fore.LIGHTRED_EX+"¿Cual es tu edad? "+Style.RESET_ALL)
age = int(input(prompt))    
print(age)
print(type(age))
print(age>=18)

if age>=18:
    print(Fore.LIGHTGREEN_EX+"Eres Adulto"+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+"Eres niño"+Style.RESET_ALL)
print("\n")"""
"""
print(Fore.LIGHTCYAN_EX+"----------While---------".title()+Style.RESET_ALL+"\n")
contador = 0
while contador<5:
    print("Hola")
    time.sleep(0.5)
    contador= contador +1
"""
"""
meesage = ""
while meesage != "salir": 
    meesage = input(Fore.LIGHTBLUE_EX+"¿Quieres continuar?, sino escribe salir ".title()+Style.RESET_ALL)
    if meesage == "salir":
        print(Fore.LIGHTGREEN_EX+"Saliendo"+Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX+"Escribe salir para Acabar"+Style.RESET_ALL)
    print(meesage)
"""
while True:
    print("alan")
    print("valente")
    prompt = "Quieres imprimir otro nombre?, Esribelo"+\
        "Si quieres salir, tipea quit"
    message = input(prompt)
    if message == 'quit' or message == 'exit' or message == 'salir':
        break
print(message)
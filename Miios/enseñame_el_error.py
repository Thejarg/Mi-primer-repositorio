from colorama import Fore, Style
import colorama
colorama.init()
import pyfiglet
X = "hola"
Hola = input(Fore.LIGHTGREEN_EX+"Porfavor dime lo primero que se te venga a la mente  "+Style.RESET_ALL)
if Hola == X:
    print(Fore.LIGHTBLUE_EX+" siii tenemos la misma idea"+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+" noooo no tenemos las mismas ideas"+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX+f" Nooooo mi palabra era {X}"+Style.RESET_ALL)
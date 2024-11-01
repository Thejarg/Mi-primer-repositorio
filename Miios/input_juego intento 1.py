"""
El proposito de este trabajo es que cuando entre un nombre especifico le mande un mensaje
sino mande otra cosa
"""
from colorama import Fore, Style

# Inicializar Colorama
import colorama
colorama.init()
nombre = "monrroy"
Name = input(Fore.LIGHTRED_EX + "Hola,".upper()+Style.RESET_ALL+ Fore.RED +"\n¿Dime cual es tu nombre?".upper() + Style.RESET_ALL)
if Name == nombre:
   print(Fore.LIGHTGREEN_EX+"Pinche Pendejo"+Style.RESET_ALL)
else:
   print(Fore.LIGHTRED_EX+f"ohhh {Name}, No se quien seas"+Style.RESET_ALL)
   

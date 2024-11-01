from colorama import Fore, Style

# Inicializar Colorama
import colorama
colorama.init()

print("------------------ Actividad 1 ------------------")
Name = input(Fore.LIGHTRED_EX + "Hola,".upper()+Style.RESET_ALL+ Fore.RED +"\n¿Dime cual es tu nombre?".upper() + Style.RESET_ALL)
print("Ohh"+" "+ Fore.LIGHTMAGENTA_EX+Name+Style.RESET_ALL+", "+"\nQue bonito nombre :3 ")
print("\n------------------ Actividad 2 ------------------")
print(Fore.LIGHTCYAN_EX + Name.upper()+ Style.RESET_ALL + " (Este es tu nombre todo en mayusculas)")
print("\n")
print(Fore.LIGHTYELLOW_EX +Name.lower()+ Style.RESET_ALL + " (Este es tu nombre todo en minusculas)")
print("\n")
print(Fore.LIGHTBLUE_EX + Name.title()+ Style.RESET_ALL +" (Este es tu nombre con la primera letra en mayusculas")

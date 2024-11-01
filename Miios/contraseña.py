from colorama import Fore, Style

# Inicializar Colorama
import colorama
colorama.init()
import pyfiglet
R = ("Seguridad")
Z = pyfiglet.figlet_format(R)
print(Z)
print("\n"+"\n"+"\n"+"\n")
W = ("Porfavor, Vuelve a Digitar tu contraseña\t".title())
U = ("\n"+ "Porfavor, Crea una contraseña\t".title())
F = input(Fore.LIGHTCYAN_EX+(U)+Style.RESET_ALL)
Z = input(Fore.LIGHTCYAN_EX+(W)+Style.RESET_ALL)

if F == Z:
    print(Fore.LIGHTGREEN_EX + "Contraseña Guardada correctamente".title() + Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX + "las contraseñas no coinciden".title() + Style.RESET_ALL)
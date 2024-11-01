from colorama import Fore, Style

# Inicializar Colorama
import colorama
import pyfiglet
colorama.init()
R = ("Seguridad")
Z = pyfiglet.figlet_format(R)
print(Z)

F = input("Porfavor, Crea una contraseña")
Z = input("Porfavor, Vuelve a Digitar tu contraseña")

if F == Z:
    print(Fore.LIGHTGREEN_EX+"\nContraseña Guardada correctamente".title()+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+"\nlas contraseñas no coinciden".title()+Style.RESET_ALL)
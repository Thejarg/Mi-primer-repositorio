from colorama import Fore, Style
import colorama
colorama.init()
import pyfiglet
r = ("seguridad".title())
Z = pyfiglet.figlet_format(r)
print(Z)
print("\n" * 4)
c = (Fore.LIGHTCYAN_EX+"Hola porfavor digita tu contraseña\t".title()+Style.RESET_ALL)
v = (Fore.LIGHTCYAN_EX+"Porfavor, vuelve a escribir la contraseña\t".title()+Style.RESET_ALL) 
Z = input(c)
X = input(v)

if Z == X:
    print(Fore.LIGHTGREEN_EX+"\nLa contraseña ha sido guardada correctamente".title()+Style.RESET_ALL)

    B = input(Fore.LIGHTMAGENTA_EX+"\nPorfavor ingrese su contraseña\t".title()+Style.RESET_ALL)

    if Z == B:
       print(Fore.LIGHTGREEN_EX+"\nContraseña correcta".title()+Style.RESET_ALL)
    else:
       print(Fore.LIGHTRED_EX+"\nLa contraseña es incorrecta".title()+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+"Las contraseñas no coinciden"+Style.RESET_ALL)

from colorama import Fore, Style

# Inicializar Colorama
import colorama
colorama.init()
import pyfiglet

r = "Seguridad".title()
Z = pyfiglet.figlet_format(r)
print(Z)
print("\n" * 4)

c = Fore.LIGHTCYAN_EX + "Hola, por favor digita tu contraseña:\t".title() + Style.RESET_ALL
v = Fore.LIGHTBLUE_EX + "Por favor, vuelve a escribir la contraseña:\t".title() + Style.RESET_ALL 

# Pedir las contraseñas
Z = input(c)
X = input(v)

# Comparar las contraseñas
if Z == X:
    print(Fore.LIGHTGREEN_EX + "\nLa contraseña ha sido guardada correctamente".title() + Style.RESET_ALL)
    
    # Solo continuar si las contraseñas coinciden
    B = input(Fore.LIGHTMAGENTA_EX + "\nPor favor ingrese su contraseña nuevamente:\t".title() + Style.RESET_ALL)

    # Comparar la contraseña ingresada con la original
    if Z == B:
        print(Fore.LIGHTGREEN_EX + "\nContraseña correcta".title() + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + "\nLa contraseña es incorrecta".title() + Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX + "\nLas contraseñas escritas no coinciden".title() + Style.RESET_ALL)

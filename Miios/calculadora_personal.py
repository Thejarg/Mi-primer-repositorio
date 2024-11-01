from colorama import Fore, Style
import colorama
colorama.init()
import pyfiglet
r = ("Calculadora".title())
Z = pyfiglet.figlet_format(r)
print(Z)
print("\n" * 4)

def suma(A, B):
    return A + B
def resta(A, B):
    return A - B
def multi(A, B):
    return A * B
def divi(A, B):
    if B == 0:
         return (Fore.LIGHTRED_EX+"No se puede dividir entre 0"+Style.RESET_ALL)
    return A / B

def calculadora():
    print(Fore.LIGHTCYAN_EX+"\n"+"Bienvendio a tu calculadora, porfavor selecciona lo que quieres hacer"+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX+"\n"+"(1)-SUMAR"+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX+"(2)-RESTAR"+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX+"(3)-MULTIPLICAR"+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX+"(4)-DIVIDIR"+Style.RESET_ALL)
    
    Elegir =input(Fore.LIGHTBLUE_EX+"Escoge Lo que quieres poniendo (1/2/3/4): "+Style.RESET_ALL)
    
    if Elegir in ['1', '2', '3', '4']:
        num1 = float(input(Fore.LIGHTWHITE_EX+"Porfavor Ingrese su primer numero:  "+Style.RESET_ALL))
        num2 = float(input(Fore.LIGHTWHITE_EX+"Porfavor Ingrese su segundo numero:  "+Style.RESET_ALL))
        if Elegir == '1':
            print(Fore.LIGHTGREEN_EX+f"{num1} + {num2} = {suma(num1,num2)}"+Style.RESET_ALL)
        if Elegir == '2':
            print(Fore.LIGHTGREEN_EX+f"{num1} - {num2} = {resta(num1,num2)}"+Style.RESET_ALL)
        if Elegir == '3':
            print(Fore.LIGHTGREEN_EX+f"{num1} * {num2} = {multi(num1,num2)}"+Style.RESET_ALL)
        if Elegir == '4':
            print(Fore.LIGHTGREEN_EX+f"{num1} / {num2} = {divi(num1,num2)}"+Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX+" Lo siento, no puede hacer lo solicitado,\n Porfavor vuelve a escoger (1/2/3/4)"+Style.RESET_ALL)
calculadora()
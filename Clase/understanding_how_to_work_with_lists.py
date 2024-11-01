from colorama import Fore, Style

# Inicializar Colorama
import colorama
import pyfiglet
colorama.init()
print("\n"*4+Fore.LIGHTGREEN_EX+"--------------Imprimir sin poner print uno por uno---------------"+Style.RESET_ALL)
#vamos a aprender a como recorrer una lsita
motor8s = ['honda','BMW','bugati']
for motor8 in motor8s:
        print(Fore.LIGHTYELLOW_EX+motor8.title()+Style.RESET_ALL)
        print(motor8.title()+ " Es un gran carro".title())
"""
---------------------------------------------------------------------------------------------------------------------------
Esto de aqui me sirve para que de una lista en lugar de tener que imprimir uno por uno pueda imprimirlos
todos con un solo print
---------------------------------------------------------------------------------------------------------------------------
"""
print("\n"+Fore.LIGHTMAGENTA_EX+"--------------Reyes-------------------"+Style.RESET_ALL)    
reyes = ['david','salomon','tutancamon']
for rey in reyes:
    print(Fore.LIGHTCYAN_EX+rey.title()+Style.RESET_ALL)
    print(rey.title() + " Es un gran rey" +f"\nOh larga vida mi señor {rey}!")
print("\n"+Fore.LIGHTBLUE_EX+"Gracias oh reyes por su ayuda"+Style.RESET_ALL)

print(Fore.LIGHTBLUE_EX+"\n"+"---------------Carritos---------------".title()+Style.RESET_ALL)
car = ['chevy','Kia','Mercedes']
for cars in car:
    print(cars.title())


print(Fore.LIGHTCYAN_EX+"---------------Rangos de numeros---------------"+Style.RESET_ALL)

Numbers = (list(range(0, 31)))
print(Fore.LIGHTRED_EX+str(Numbers)+Style.RESET_ALL)
print(Fore.LIGHTCYAN_EX+"\n"+"---------------Rangos de numeros uno por uno---------------"+Style.RESET_ALL)
for number in Numbers:
    print(Fore.LIGHTYELLOW_EX+str(number)+Style.RESET_ALL)
    
print(Fore.LIGHTCYAN_EX+"---------------Rangos de numeros Pares e impares---------------"+Style.RESET_ALL)
par = (list(range(2,11,2)))# El primer 2 es el numero por el que se va a sumar con el 2 del final y el 11 es el limite con el que se puede llegar (para que no sea infinito)
print(par)
for im in par:
    print(Fore.RED+str(im)+Style.RESET_ALL)   
impar = (list(range(3,11,2)))
print(impar)
for imaas in impar:
    print(Fore.BLUE+str(imaas)+Style.RESET_ALL)
    

print(Fore.BLUE+"------------Actividad linea del uno al 100(personal)---------------"+Style.RESET_ALL)

X = list(range(1,11))
print(X)
for z in X: 
    print(z**2)

print(Fore.BLUE+"------------Actividad linea Del profe A su gusto---------------"+Style.RESET_ALL)
sq = []
for value in range(1,11): 
    sq.append(value**2)
print(sq)
print(Fore.LIGHTCYAN_EX+"---------------list completacion---------------"+Style.RESET_ALL+"\n"*2)
numeros2 = [number5 for number5 in range (1,11)]
print(numeros2)
numeros3 = [number4**2 for number4 in range (1,11)]
print(numeros3)

print(Fore.YELLOW+"------------Salto de linea de 2 listas---------------"+Style.RESET_ALL)

carritos = ['honda','BMW','Susuki']
helados = ['chocolate','fresa','vainilla']
for value in range(0,3):
    print(carritos[value]+"\n"+helados[value]+"\n")
print(Fore.LIGHTCYAN_EX+"------------Darme el minimo el maximo y la suma de todos---------------"+Style.RESET_ALL)
numeros = list(range(0,21))
print("\nEl minimo de la lista")
print(min(numeros))
print("\nEl maximo de la lista")
print(max(numeros))
print("\nLa suma de la lista")
print(sum(numeros))

print(Fore.LIGHTCYAN_EX+"------------SLICING O SLICE---------------"+Style.RESET_ALL+"\n")
## SLICING O SLICE

players = ['charly','doria','jose maria','valente','puga']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(Fore.LIGHTCYAN_EX+"------------Slicing EN UN FOR---------------"+Style.RESET_ALL+"\n")

## Slicing EN UN FOR 
players = ['charly','doria','jose maria','valente','puga','requena']
print("Aqui se presentan los primeros 3 alumnos")
for player in players[0:3]:
    print(player)
print(Fore.LIGHTCYAN_EX+"------------Copia de listas---------------"+Style.RESET_ALL+"\n")
## Copia de listas
mi_food = ['pollito','chilaquiles','Flautas']
Comida_favorita = mi_food[:]
Comida_favorita = list(mi_food)
Comida_favorita = mi_food.copy()
mi_food.append('taquitos')
print(mi_food)
print(Comida_favorita)

print(Fore.LIGHTCYAN_EX+"------------Tuplas/Inmutables---------------"+Style.RESET_ALL+"\n")
##Tuplas
"""
la tuplas son listas de elementos que no se cambian 
las tuplas son listas inmutables
se utilizan () para definir la tupla
"""
dimensiones = (200, 500)
print(dimensiones)
print("\n")
print("forma manual de imprimir uno por uno")
print(dimensiones[0])
print(dimensiones[1])
print("\n"+"Una Forma de imprimirlos uno por uno")
for dimension in dimensiones:
    print(dimension)
dimensiones = (250, 500)
print("\n"+"La unica forma de cambiar un valor inmutable")
print(dimensiones)
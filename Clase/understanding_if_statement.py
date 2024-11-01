from colorama import Fore, Style

# Inicializar Colorama
import colorama
import pyfiglet
colorama.init()
print(Fore.LIGHTCYAN_EX+"----------Usar algo de una lista de forma especifico---------".title()+Style.RESET_ALL)
cars =['bochito','mustang','bugati','honda']
for car in cars:
    if car == 'mustang': #Define carro es igual a mustang haga algo
        print(car. upper()+"\n") #Aqui definimos que se imprima en mayusculas todo
    else:
        print(car.title()+"\n") #si no es imprime solo la primera letra en mayuculas
        


print(Fore.LIGHTCYAN_EX+"----------Practica mia(Multi lista)---------".title()+Style.RESET_ALL)
##Crear una lista que se repita varias veces

X = ['Yepez ']
Z = ['Nahim ']
V = ['Josue ']
for value in range(0,12):
    print([value]+(X+Z+V))
    
print("\n"*2+Fore.LIGHTCYAN_EX+"----------Condicionales true/false---------".title()+Style.RESET_ALL+"\n")
"""
CONDICIONALES- los condicionales son el corazon de un if
"""
#Condicional que tiene como resultado true
carro = 'Honda'
print(carro == 'Honda')

#Condicional que tiene como resultado un false
Perro = 'choco'
print(Perro == 'gato')

Carrito = 'Audi'
print(Carrito.lower() == 'audi')
print("\n"*2+Fore.LIGHTCYAN_EX+"----------Desigualdades---------".title()+Style.RESET_ALL+"\n")
#Condicional != para determinar una igualdad
tacos = 'trompo'
print(tacos!='pastor')
print("\n"*2+Fore.LIGHTCYAN_EX+"----------#######---------".title()+Style.RESET_ALL+"\n")

## 
age = 18
print(age==18)
answar = 17
print(answar!=42)
age = 19
print(age<21)  ###Compara las edades siendo si son mayor o menos que lo ya dictado
print(age<=21)
print(age>21)
print(age>=21)

print("\n"*2+Fore.LIGHTCYAN_EX+"----------Multiple conditions---------".title()+Style.RESET_ALL+"\n")
"""
Multiple conditions
"""
age_0 = 22
age_1 = 18
print(age_0>21 and age_1>=21)
print(age_0>21 or age_1>=21)

"""
And = si los 2 son True va a dar el resultado En true en caso de que uno de los 2 no sean verdad va a dar false

Or = Con que uno sea igual o lo que pide, Va a dar true y para que de false los 2 tienen que ser incorrectos


NOTA: Como las compuertas logicas

"""
print("\n"*2+Fore.LIGHTCYAN_EX+"----------Como nos preguntamos si un valor esta en  una lista???---------".title()+Style.RESET_ALL+"\n")
##Como nos preguntamos si un valor esta en  una lista

alumnos = ['Andres','Doria','Tovar']
## Como ale no esta en la lista nos va a mandar false, pero como Doria si esta en la lista nos va a mandar un True
print('ale' in alumnos)
print('Doria' in alumnos)
## Ahora hacemos lo contrario que buscar que no este en la lista
print('ale' not  in alumnos)
print('Doria' not in alumnos)

print("\n"*2+Fore.LIGHTCYAN_EX+"----------fibunacci alan---------".title()+Style.RESET_ALL+"\n")
numeros = []
n, m = 0, 1
for value in range(10):
    numeros.append(n)
    n, m = m, n + m
print (numeros)

print("\n"*2+Fore.LIGHTCYAN_EX+"----------Programa Profe---------".title()+Style.RESET_ALL+"\n")
j =5
fibuu = [0,1]
for value in range(0,j-2):
    fib = fibuu[-1]+fibuu[-2]
    fibuu.append(fib)
print(fibuu)
print("")
a = 0 
b = 1
print(a)
print(b)
for _ in range (0,j-2):
    fib = a+b
    print(fib)
    a = b
    b= fib 
    
print("\n"*2+Fore.LIGHTCYAN_EX+"----------clase profe dia 24/10/2024---------".title()+Style.RESET_ALL+"\n")

age = 19
if age <=4:
    price = 0
elif age<=18:
    price = 500
elif  age<65:
    price=500
else:
    price = 100
print(f"Tu Entrada esta en ${price}")
print("\n"*2)
###
guisos = ['desebrada','salsa verde']
if 'desebrada' in guisos:
    print("Hay desebrada!!")
if 'salsa verde' in guisos:
    print("Hay salsa verde!!")
if 'picadillo' in guisos:
    print("Hay picadillo")
else:
    print("No hay picadillo")
print("Estos son los guisos")
print("")


if 'salsa verde' in guisos:
    print('Hay salsa verde')
elif 'desebrada' in guisos:
    print("Hay desebrada")   
elif 'chicharron' in guisos:
    print('hay chicharron')
else:
    print("No hay ningun guiso") 
    
### Empty
gui = []
if gui:
    print("Hay elementos")
else:
    print("no hay elementos")
    
###

dispo = ['salsa verde','desebrada','picadillo','huevo con chorizo']
orde = ['chicarron','desebrada','huevo con chorizo']
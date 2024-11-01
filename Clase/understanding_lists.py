"""
Las listas nos permiten almmacenar informacion en un lugar, la cantidad de elementos que desees:
ya sean pocos elementos o miles, o millones, etc.

En python los corchetes [] indican o definen un lista, 
sus elementos se separan por comas.


EJEMPLO:
"""
        #0      #1            #2          #3
        #0      #-3           #-2         #-1
JR = [('TREK','CANNONDALE','REDLINE','SPECIALIZED'.title())]
print(JR)

anng = [('Agua','fuego','tierra','aire'.title())]
print(anng)
"""
1. Almacena los nombres de algunos de tus amigos
en una lsita llamada names. imprime el nombre de tus amigos uno por uno accediendo 
a los elementos de la lista.

2. Utiliza la lista anterior. imprime el nombre de la persona agragandole un mensaje, es decir, el texto del mensaje 
debe ser el mismo, pero cada mensaje debe estar presonalizado con nombre de la persona

3. crea una lista con algunos metodos de transporte.
utilioza la lista para imprimir una serie de mensajes
sobre cada elemento de la lista.

Por ejemplo: "me gustaria tener un Auto Tesla"

"""
names = ['Monrroy','rocket','alejandra','andres','doria','yepeto','felipa','nahim','ricardo']

#Agrega elementos a una lista
print("\n---------Agregar Elementos a una lista".title())
motor = ['Honda','mortalica','yahama','suzuki']
print("\n"+"\n"+str(motor))
motor.append('italika')
print("\n"+"\n"+str(motor))

motor2 = [] #Esto es una lista VACIA
motor2.append('yahama')
motor2.append('suzuki')
motor2.append('honda')
print("\n"+"\n"+str(motor2))

print("\n------------------METODO AGREGAR EN UN PUNTO ESPECIFICO-------------------".title())
motor3 = ['Honda','yahama','suzuki']
print(motor3)
motor3.insert(1,'bugati')
print(motor3)
print("\n------------------METODO BORRAR-------------------".title())
motor4 = ['honda','yahama','suzuki']
print(motor4)
del motor4[0]
print(motor4)
print("\n--------------Metodo POP---------------------")
"""
METODO POP
"""
#ELIMINA EL ULTIMO ELEMENTO DE LA LISTA, PERO NOS PERMITE UTILIZAR 
#ESTE ELEMENTO DESPUES DE UTILIZARLO

motor5 = ['honda','yahama','suzuki']
print(motor5)

poped = motor5.pop()
print(motor5)
print (f"la motocicleta eliminada fue {poped}")
#El metodo pop tambien se puede utilizar para eliminar un elemento
#Especifico de la lista
motor5.pop(0)
print("\nUsamos el comando motor.pop(0)(0 es el valor donde esta acomodado)")
print(motor5)
print("\n"*2+"-------------METODO Remove----------------------------")
#Metodo Remove
#Permite Eliminar elementos por su valor
motor6 = ['honda','yahama','suzuki']
print(motor6)
motor6.remove('honda')
print(motor6)
print("\n"*3 +"---------------Eliminacion Especifico---------------")
motor7 = ['Honda','Yahama','suzuki','bugati']
print(motor7)
Resa = "bugati"
motor7.remove(Resa)
print(motor7)
print(f"El elemento {Resa} se ha eliminado")
#Este es otro metodo para poder eliminar un elemento de forma especifica

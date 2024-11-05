from colorama import Fore, Style

# Inicializar Colorama
import colorama
import pyfiglet
colorama.init()
"""
    Ejercicio.
        1. Almacena un mensaje en una variable e imprímelo.
        2. Almacena un mensaje en una variable e imprímelo. 
        Luego cambia el valor de la variable a otro mensaje
        e imprime el nuevo mensaje.
"""
print(Fore.LIGHTCYAN_EX+"-----------Ejercicios Understanding Variables--------------".title()+Style.RESET_ALL)
X = "josue"
print(X)
z = "Esteban"
print(z)
z = "Emma"
print(z)
print("\n")
print(Fore.LIGHTCYAN_EX+"-----------Ejercicios understanding strings--------------".title()+Style.RESET_ALL)
"""
    Ejercio:
    
    1. Guarda el nombre de una persona en una variable e imprime 
    un mensaje de bienvenida a esa persona, ejemplo de la salida :
    " Hola Charly, ¿te gustaría aprender algo más sobre python?"
"""
print("")
print(Fore.LIGHTGREEN_EX+"Primer Ejercicio:"+Style.RESET_ALL)
W = "henry"

print(f"Hola {W},¿Estas listo para ser la mejor persona que existe? ")
""" 
    2. Guarda el nombre de una persona en una variable e imprime
    su nombre en minúsculas, mayúsculas y utilizando el método title.
""" 
print("")
print(Fore.LIGHTGREEN_EX+"Segundo Ejercicio:"+Style.RESET_ALL)
E = "ESteBan"
print(E)
print(E.lower())
print(E.upper())
print(E.title())
""" 
    3. Encuentra una cita de alguna persona famosa. Imprime la cita
    y el nombre del autor. Por ejemplo:
    "Charly Mercury una vez dijo, 'Python is love'"
""" 
print("")
print(Fore.LIGHTGREEN_EX+"Tercer Ejercicio:"+Style.RESET_ALL)
print("Mahatma Gandhi una vez dijo, 'No hay caminos para la paz; la paz es el camino'")
"""     
    4. Repite el ejercicio anterior, pero ahora almacena el nombre
    de la persona famosa en una variable famous_person. Ahora
    crea la variable para la cita e imprime el mensaje.
""" 
print("")
print(Fore.LIGHTGREEN_EX+"Cuarto Ejercicio:"+Style.RESET_ALL)
F = "Mahatma Gandhi"
print(f"{F} Alguna vez dijo,'No hay caminos para la paz; la paz es el camino'")
""" 
    5. Guarda el nombre de una persona en una variable,
    agrega espacios, 
    tabuladores, saltos de línea. Imprime el nombre, 
    después 
    el nombre varias veces utilizando los métodos 
    rstrip, lstrip, strip.
"""
print("")
print(Fore.LIGHTGREEN_EX+"Quinto Ejercicio:"+Style.RESET_ALL)
H = "\n  \t Emma,Esteban  \t"
print(H)
print(H.rstrip("2"))
print(H.lstrip())
print(H.strip())

"""
    Ejercicios: 

        - Escribe una suma, resta, multiplicación y división
        en la que cada resultado sea 8.
        - Almacena tu número favorito en una variable. Luego
        utilziando esta variable crea un mensaje que revele
        cual es tu número favorito. Finalmente, imprime
        el mensaje.
"""
print(Fore.LIGHTCYAN_EX+"-----------Ejercicios Understanding Numbers--------------".title()+Style.RESET_ALL)
print(4+4)
print(12-4)
print(4*2)
print(16/2)
E = 7
print("Mi numero favorito es " +str(E))
print(Fore.LIGHTCYAN_EX+"-----------Ejercicios Understanding List--------------".title()+Style.RESET_ALL)

"""


    Ejercicios:
    
    1. Almacena los nombres de algunos de tus amigos 
    en una lista llamada names. Imprime el nombre de 
    tus amigos de uno por uno, accediendo a los
    elementos de la lista.     
    2. Utilizando la lista anterior. Imprime el nombre
    de la persona agregándole un mensaje. El texto del 
    mensaje debe ser el mismo, pero cada mensaje debe 
    estar personalizado con el nombre de la persona.
    3. Crea una lista con tus métodos favoritos de 
    transporte. Utiliza la lista para imprimir una
    serie de mensajes sobre cada elemento de la lista,
    por ejemplo, "Me gustaría tener un auto Tesla".
    
"""
print(Fore.LIGHTGREEN_EX+"Ejercicio 1:"+Style.RESET_ALL)
Names = ['yepez','doria','nahim']
for name in Names:
    print("Hola "+name.title()+",¿Como estas? Tiempo sin verte")
print("")
Transporte = ['Kia','honda','Camioneta']
for transpor in Transporte:
    print(f"Me Encantaria tener una {transpor.title()},Estan muy bonitos")


"""

    Ejercicios.

    1. Piensa en al menos tres tipos de pizzas que te gusten mucho. 
    Guarda los nombres de estas pizzas en una lista y luego utiliza 
    un ciclo for para imprimir el nombre de cada pizza.

        a) Modifica el ciclo for para que imprima una oración completa, 
        en lugar de solo el nombre de la pizza. Por ejemplo, en lugar de 
        solo imprimir "pepperoni", el programa debe mostrar: 
        "Me gusta la pizza de pepperoni".

        b) Al final del programa, fuera del ciclo for, agrega una línea 
        que diga cuánto te gusta la pizza en general. Por ejemplo, después 
        de las oraciones de las pizzas específicas, podrías agregar algo 
        como: "¡Realmente me encanta la pizza!".
    
    2. Piensa en al menos 3 animales diferentes que tengan características
    similares. Almacenalos en una lista e imprime el nombres de cada animal
    utilizando un for. 
    
        a) Imprime un mismo mensaje para cada animal, por ejemplo: " un perro
        sería una gran mascota. "
        
        b) Agrega un elemento al final de tu programa e imprímelo, 
        por ejemplo: " Todos éstos animales serían una gran mascota" 

"""
print(Fore.LIGHTCYAN_EX+"-----------Ejercicios Understanding how_to_work_with_lists--------------".title()+Style.RESET_ALL)
print("")
print(Fore.LIGHTGREEN_EX+"Ejercicio 1:"+Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX+"1:"+Style.RESET_ALL)
pizza = ['hawaiana','pepperoni','carnes']
for pisa in pizza:
    print(f"Mi pizza favorita es la pizza de {pisa}")
print("Pero he de decir que ME ENCANTA LA PIZZA")
print(Fore.LIGHTMAGENTA_EX+"2:"+Style.RESET_ALL)
animales = ['gato','perro','pajaro']
for ani in animales:
    print(f"Un {ani},Seria una buena idea para una mascota")
print(Fore.LIGHTYELLOW_EX+"No importa cual sea, Cualquiera de estos animales seria una gran mascota"+Style.RESET_ALL)
"""

    Ejercicios: 

        1. Utiliza el for loop para imprimir los números del 1 al 20.
        2. Construye una lista de números del 1 al 1000000 y utiliza
            un for para imprimir los números. (En caso de ser necesario 
            utiliza ctrl+c para parar el progra).
        3. Utiliza la lista anterior para saber cual es el mínimo y el 
            máximo de una lista. Suma los números utilizando sum.
        4. Utiliza el tercer argumento de range() para hacer una lista
            que contenga los números pares del 1 al 20. Utiliza un for 
            para imprimir los valores de la lista.
        5. Crea una lista que contenga múltiplos de 3 del 3 al 30. 
            Utiliza un for para imprimir los valores de la lista.
        6. Un número elevado a la tercera potencia es llamado un cubo.
            Por ejemplo, el cubo de 2 se escribe en Python 2**3. Crea
            una lista con los primeros 10 cubos (1^3, 2^3, 3^3, ... , 10^3).
            Utiliza un for para imprimir los valores de la lista.
        7. Utiliza una list comprehension para generar una lista de los 
            primeros 20 cubos. Utiliza un for para imprimir los valores de 
            la lista.
"""
print("")
print(Fore.LIGHTGREEN_EX+"Ejercicio 2:"+Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX+"1:"+Style.RESET_ALL)
for number in range(0,21):
    print(number)
print(Fore.LIGHTMAGENTA_EX+"\n"+"2:"+Style.RESET_ALL)    
G = []
for lists2 in list(range(0,101)):
    G.append(lists2)
print(G)
print(Fore.LIGHTRED_EX+"Se que son 1000000, Pero eran muchos numeros y se me petaba la pc"+Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX+"\n"+"3:"+Style.RESET_ALL) 
lists3 = list(range(0,101))
print(min(lists3))
print(max(lists3))
print(sum(lists3))
print(Fore.LIGHTMAGENTA_EX+"\n"+"4:"+Style.RESET_ALL)
FG = []
for lista5 in range(0,21,2):
    FG.append(lista5)
print(FG)
FR =[]
print(Fore.LIGHTMAGENTA_EX+"\n"+"5:"+Style.RESET_ALL)
for lista6 in range (0,31,3):
    FR.append(lista6)
print(FR)
print(Fore.LIGHTMAGENTA_EX+"\n"+"6:"+Style.RESET_ALL)
RG =[]
for lista7 in range(0,11):
    vls = lista7**3
    RG.append(vls)
print(RG)
    
print(Fore.LIGHTMAGENTA_EX+"\n"+"7:"+Style.RESET_ALL)
DR = []
cubo =[numero**3 for numero in range(0,21)]
for cubos in cubo:
    DR.append(cubos)
print(DR)

"""


    Ejercicios: 
    
    
        1. Rebanadas: Usa uno de los programas que escribiste en el ejercicio
            anterior, agrega varias líneas al final del programa que hagan lo
            siguiente:
            
            - Imprime el mensaje: Los primeros tres elementos en la lista
                son: Luego usa una rebanada (slice) para imprimir los primeros
                tres elementos de la lista de ese programa.
            - Imprime el mensaje: Tres elementos del medio de la lista son:
                Usa una rebanada para imprimir tres elementos del medio de
                la lista.
            - Imprime el mensaje: Los últimos tres elementos de la lista son:
                Usa una rebanada para imprimir los últimos tres elementos de
                la lista.
        
        2. Mis Pizzas, Tus Pizzas: Comienza con tu programa del Ejercicio de
            las pizzas. Haz una copia de la lista de pizzas y llámala
            friend_pizzas. Luego, haz lo siguiente:

            - Agrega una nueva pizza a la lista original.
            - Agrega una pizza diferente a la lista friend_pizzas.
            - Demuestra que tienes dos listas separadas.
                - Imprime el mensaje: Mis pizzas favoritas son:, y luego usa
                    un bucle for para imprimir la primera lista.
                - Imprime el mensaje: Las pizzas favoritas de mi amigo son:
                    y luego usa un bucle for para imprimir la segunda lista.
                    Asegúrate de que cada nueva pizza esté almacenada en la
                    lista correspondiente.

"""
print("")
print(Fore.LIGHTGREEN_EX+"Ejercicio 3:"+Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX+"1:"+Style.RESET_ALL)
Agua = ['jamaica','limon','fresa','platano','horchata']
print(Fore.LIGHTBLUE_EX+"Los primeros 3 Elementos de la lista son: "+Style.RESET_ALL + f"{Agua[0:3]}".title())
print(Fore.LIGHTBLACK_EX+"---Esto es una forma de imprimirlo---"+\
    "La otra forma seria:"+Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX+"Los primeros 3 elementos de la lista son:"+Style.RESET_ALL)
for aguas in Agua[0:3]:
    print(aguas.title())
print(Fore.LIGHTRED_EX+"Los ultimos 3 elementos de la lista son:"+Style.RESET_ALL)
for agua2 in Agua[2:5]:
    print(agua2.title())
print(Fore.LIGHTMAGENTA_EX+"2:"+Style.RESET_ALL)
Mispizzas = ['pepperoni','3_carnes','hawaiana']
copia = Mispizzas.copy()
copia.append('3_Quesos')
Mispizzas.append('suprema')
print(Fore.LIGHTGREEN_EX+f"mis pizzas favoritas son"+Style.RESET_ALL)
for pizzasss in Mispizzas:
    print(Fore.LIGHTBLACK_EX+pizzasss.title()+Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX+f"Las pizzas favoritas de mi amigo son"+Style.RESET_ALL)
for pizzasssssss in copia:
    print(Fore.LIGHTBLACK_EX+pizzasssssss.title()+Style.RESET_ALL)



"""
    Ejercicios: 
        
    (1)  Pruebas Condicionales: Escribe una serie de pruebas condicionales.
        Imprime una declaración que describa cada prueba y tu predicción 
        para el resultado de cada prueba. Tu código debería verse algo así:
            car = 'bocho'
            print("¿Es car == 'bocho'? Predigo que es True.")
            print(car == 'bocho')
            print("\n¿Es car == 'audi'? Predigo que es False.")
            print(car == 'audi')      
    (2)   Observa de cerca tus resultados y asegúrate de entender por qué 
        cada línea se evalúa como True o False. Crea al menos 10 pruebas.
        Haz que al menos 5 pruebas se evalúen como True y otras 5 se evalúen 
        como False.
    (3)  Más Pruebas Condicionales: No tienes que limitar el número de pruebas
        a 10. Si quieres intentar más comparaciones, escribe más pruebas y 
        añádelas a tu script. Asegúrate de tener al menos un 
        resultado True y un resultado False para cada uno de los siguientes 
        casos:

            - Pruebas de igualdad y desigualdad con strings.
            - Pruebas usando la función lower().
            - Pruebas numéricas que involucren igualdad y desigualdad, mayor 
                que y menor que, mayor o igual que y menor o igual que.
            - Pruebas usando la palabra clave and y la palabra clave or.
            - Prueba si un elemento está en una lista.
            - Prueba si un elemento no está en una lista.
"""
print(Fore.LIGHTRED_EX+"-----------Ejercicios Understanding statements--------------".title()+Style.RESET_ALL)
print(Fore.LIGHTCYAN_EX+"--------------Primer tomo de ejercicios--------------".title()+Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX+"Ejercicios 1:"+Style.RESET_ALL)
taquitos = 'bistec'
print(Fore.LIGHTGREEN_EX+"¿taquitos == 'bistec'? ".title()+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"Predigo que es True"+Style.RESET_ALL)
print(f"La respuesta es {taquitos == 'bistec'}")
print(Fore.LIGHTRED_EX+"¿taquitos == 'cabeza'? ".title()+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"Predigo que es False"+Style.RESET_ALL)
print(f"La respuesta es {taquitos == 'Cabeza'}")

############################################################################################################################################################################################

print(Fore.LIGHTMAGENTA_EX+"Ejercicios 2"+Style.RESET_ALL)

name1, name2, name3, name4, name5 = 'Josue', 'Emma', 'Esteban', 'Adriana','Dana'
###Para no Equivocarme entre los True o False, Cree unos nombres especificos para ponerlos como True y otra para ponerlos como False
namefalse1, namefalse2, namefalse3, namefalse4, namefalse5 = 'Elaided', 'Mansur', 'Indio', 'Juan','Pedro' 

print(Fore.LIGHTGREEN_EX+"¿name1 == 'Josue'?"+Style.RESET_ALL +Fore.LIGHTBLACK_EX+" Siii, si lo es, Entonces es True"+Style.RESET_ALL)
print(name1 == 'Josue')
print("")
print(Fore.LIGHTGREEN_EX+"¿namefalse1 == 'mansur'?"+Style.RESET_ALL +Fore.LIGHTBLACK_EX+" Noo no lo seria entonces es False"+Style.RESET_ALL)
print(namefalse1 == 'mansur')
print("")
print(Fore.LIGHTGREEN_EX+"¿name2 == 'Emma'?"+Style.RESET_ALL +Fore.LIGHTBLACK_EX+" si lo es entonces es True"+Style.RESET_ALL)
print(name2 == 'Emma')
print("")
print(Fore.LIGHTGREEN_EX+"¿namefalse2 == 'indio'?"+Style.RESET_ALL +Fore.LIGHTBLACK_EX+" Noo no lo seria entonces es False"+Style.RESET_ALL)
print(namefalse2 == 'indio')
print("")
print(Fore.LIGHTGREEN_EX+"¿name3 == 'Esteban'?"+Style.RESET_ALL +Fore.LIGHTBLACK_EX+" Si lo es Asi que por 3 vez es True"+Style.RESET_ALL)
print(name3 == 'Esteban')
print("")
print(Fore.LIGHTGREEN_EX+"¿namefalse3 == 'Pedro'?"+Style.RESET_ALL +Fore.LIGHTBLACK_EX+" Noo no lo seria entonces es False"+Style.RESET_ALL)
print(namefalse3 == 'Pedro')
print("")
print(Fore.LIGHTGREEN_EX+"¿name4 == 'Adriana'?"+Style.RESET_ALL +Fore.LIGHTBLACK_EX+" Si lo es entonces es True"+Style.RESET_ALL)
print(name4 == 'Adriana')
print("")
print(Fore.LIGHTGREEN_EX+"¿namefalse4 == 'juan'?"+Style.RESET_ALL +Fore.LIGHTBLACK_EX+" Noo no lo seria entonces es False"+Style.RESET_ALL)
print(namefalse4 == 'Mansur')
print("")
print(Fore.LIGHTGREEN_EX+"¿name5 == 'Dana'?"+Style.RESET_ALL +Fore.LIGHTBLACK_EX+" Si lo es entonces es True"+Style.RESET_ALL)
print(name5 == 'Dana')
print("")
print(Fore.LIGHTGREEN_EX+"¿namefalse5 == 'elaided'?"+Style.RESET_ALL +Fore.LIGHTBLACK_EX+" Noo no lo seria entonces es False"+Style.RESET_ALL)
print(namefalse5 == 'elaided')
############################################################################################################################################################################################
print(Fore.LIGHTMAGENTA_EX+"Ejercicios 3"+Style.RESET_ALL)
nombre1, nombre2, nombre3, nombre4, nombre5, nombre6, nombre7, nombre8, nombre9, nombre10 = 'Josue', 'Emma', 'Esteban', 'Adriana','Dana', 'Juan', 'Pedro', 'Manuel', 'Maria', 'Carlos'
Añosmayores = range(18,100)
añosmenores = range(0,18)
print(Fore.LIGHTYELLOW_EX+"Primero Probaremos 2 De igualdad y desigualdad con strings"+Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX+"Primera prueba que verificara si el nombre Emma pertenece a nombre2 "+Style.RESET_ALL)
print(f"¿Emma Pertenece A Nombre2? = {nombre2 == 'Emma'}")
print(Fore.LIGHTRED_EX+"Ahora la prueba de desigualdad"+Style.RESET_ALL)
print(f"¿Adriana Aparece en nombre1? = {nombre1 == 'Adriana'}")
print(Fore.LIGHTYELLOW_EX+"Ahora haremos pruebas con la funcion lower()"+Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX+"Primera prueba que verificara si el nombre Josue.lower() pertenece a nombre1"+Style.RESET_ALL)
print(f"¿Josue.lower() Pertenece A Nombre1? = {nombre1 == 'Josue'.lower()}")
print(Fore.LIGHTGREEN_EX+"Ahora usaremos una variable con .lower()"+Style.RESET_ALL)
print(f"¿nombre3.lower() == 'Esteban'? = {nombre3.lower() == 'Esteban'}")
print(Fore.LIGHTGREEN_EX+"Por ultimo los 2 tendran .lower()"+Style.RESET_ALL)
print(f"¿nombre4.lower() == 'Adriana'.lower()? = {nombre4.lower() == 'Adriana'.lower()}")
print(Fore.LIGHTYELLOW_EX+"Ahora pruebas numericas"+Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX+"Sera que el numero 10 es mayor que el 5?"+Style.RESET_ALL)
print("¿10 Es mayor que 5? ="+str(10 > 5))
print(Fore.LIGHTGREEN_EX+"Si tengo 12 años entonces soy mayor de edad?"+Style.RESET_ALL)
print(f"Mi edad es 12 años entonces soy mayor de edad? = {str(12) >= str(Añosmayores)}")
print(Fore.LIGHTGREEN_EX+"Si tengo 23 años soy menor de edad?"+Style.RESET_ALL)
print(f"Mi edad es 23 años entonces soy menor de edad? = {str(23) >= str(Añosmayores)}")
print(Fore.LIGHTGREEN_EX+"Tengo 18 años de edad, entonces soy mayor de edad?"+Style.RESET_ALL)
print(f"Mi edad es 18 años entonces soy mayor de edad? = {str(18) <= str(Añosmayores)}")
print(Fore.LIGHTYELLOW_EX+"Ahora pruebas usando la palabra clave and y la palabra clave or"+Style.RESET_ALL)
PO = 'Josue'
LO = 'Dana'
if 'Josue' in PO and 'Dana' in LO:
    print(Fore.LIGHTGREEN_EX+"Los 2 son iguales"+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+"Los 2 no son iguales"+Style.RESET_ALL)
if 'Josue' in PO and 'Adriana' in LO:
    print(Fore.LIGHTGREEN_EX+"Los 2 son iguales"+Style.RESET_ALL)
else:    
    print(Fore.LIGHTRED_EX+"Los 2 no son iguales"+Style.RESET_ALL)
if 'Josue' in PO or 'Adriana' in LO:
    print(Fore.LIGHTGREEN_EX+"Uno de los 2 coincide"+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+"Ninguno de los 2 coincide"+Style.RESET_ALL)
if 'alfredo' in PO or 'Elizabeth' in LO:
    print(Fore.LIGHTGREEN_EX+"Uno de los 2 coincide"+Style.RESET_ALL)
else:    
    print(Fore.LIGHTRED_EX+"Ninguno de los 2 coincide"+Style.RESET_ALL)
print(Fore.LIGHTYELLOW_EX+"Ahora pruebas si un elemento está en una lista"+Style.RESET_ALL)
pranda = ['Josue','Adriana','Dana','Elizabeth']
print(Fore.LIGHTGREEN_EX+"¿Sera que Adriana y Dana esta en la lista pranda? "+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"\nPues Resulta que es: "+Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX+"Adriana:"+Style.RESET_ALL)
print('Adriana' in pranda)
print(Fore.LIGHTBLUE_EX+'Dana: '+Style.RESET_ALL)
print('Dana' in pranda)
print(Fore.LIGHTYELLOW_EX+"Ahora pruebas si un elemento no está en una lista"+Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX+"¿Sera que Nahim y Jorge esta en la lista pranda? "+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"\nPues Resulta que es: "+Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX+"Nahim:"+Style.RESET_ALL)
print('Nahim' in pranda)
print(Fore.LIGHTBLUE_EX+'Jorge: '+Style.RESET_ALL)
print('Jorge' in pranda)


"""

    Ejercicios: 
    
        1. Colores de Extraterrestres: Imagina que un extraterrestre acaba de
        ser derribado en un juego. Crea una variable llamada color_alien y 
        asígnale un valor de 'verde', 'amarillo' o 'rojo'.

            Escribe una declaración if para comprobar si el color del 
            extraterrestre es verde. Si lo es, imprime un mensaje indicando que 
            el jugador acaba de ganar 5 puntos. Escribe una versión de este 
            programa que pase la prueba if y otra que no la pase. 

        2. Colores de Extraterrestres : Elige un color para un extraterrestre 
        como hiciste en el ejercicio anterior, y escribe una cadena if-else.

            - Si el color del extraterrestre es verde, imprime una declaración
                que indique que el jugador acaba de ganar 5 puntos por 
                dispararle al extraterrestre.
            - Si el color del extraterrestre no es verde, imprime una 
                declaración que indique que el jugador acaba de ganar 10 
                puntos.
            - Escribe una versión de este programa que ejecute el bloque if y
                otra que ejecute el bloque else.

        3. Colores de Extraterrestres : Convierte tu cadena if-else del 
        ejercicio anterior en una cadena if-elif-else.

            - Si el extraterrestre es verde, imprime un mensaje que indique 
                que el jugador ganó 5 puntos.
            - Si el extraterrestre es amarillo, imprime un mensaje que indique
                que el jugador ganó 10 puntos.
            - Si el extraterrestre es rojo, imprime un mensaje que indique 
                que el jugador ganó 15 puntos.
            - Escribe tres versiones de este programa, asegurándote de que 
            cada mensaje se imprima para el color adecuado del extraterrestre.

        4. Etapas de la Vida: Escribe una cadena if-elif-else que determine la
        etapa de la vida de una persona. Asigna un valor a la variable edad 
        y luego:

            - Si la persona tiene menos de 2 años, imprime un mensaje que 
                indique que es un bebé.
            - Si la persona tiene al menos 2 años pero menos de 4, imprime un
                mensaje que indique que es un niño pequeño.
            - Si la persona tiene al menos 4 años pero menos de 13, imprime un
                mensaje que indique que es un niño.
            - Si la persona tiene al menos 13 años pero menos de 20, imprime 
                un mensaje que indique que es un adolescente.
            - Si la persona tiene al menos 20 años pero menos de 65, imprime 
                un mensaje que indique que es un adulto.
            - Si la persona tiene 65 años o más, imprime un mensaje que 
                indique que es un anciano.

        5. Fruta Favorita: Haz una lista de tus frutas favoritas y luego 
        escribe una serie de declaraciones if independientes que verifiquen 
        si ciertas frutas están en tu lista.

            Haz una lista de tus tres frutas favoritas y llámala 
            frutas_favoritas. Escribe cinco declaraciones if. Cada una debe
            comprobar si cierto tipo de fruta está en tu lista. Si la fruta 
            está en tu lista, el bloque if debe imprimir un mensaje, como 
            "¡Realmente te gustan las fresas!"

"""
print("")
print(Fore.LIGHTCYAN_EX+"--------------Segundo Tomo de ejercicios-------------".title()+Style.RESET_ALL)
print("")
print(Fore.LIGHTCYAN_EX+"1:"+Style.RESET_ALL)
color_alien = 'verde','amarillo','rojo'
if 'verde' in color_alien:
    print(Fore.LIGHTGREEN_EX+"Felicidades!! Tienes 5 Puntos"+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+"No tienes 5 Puntos"+Style.RESET_ALL)
color_alien = 'amarillo','rojo'
if 'verde' in color_alien:
    print(Fore.LIGHTGREEN_EX+"Felicidades!! Tienes 5 Puntos"+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+"No tienes 5 Puntos"+Style.RESET_ALL)
print("")
print(Fore.LIGHTCYAN_EX+"2:"+Style.RESET_ALL)
##### LA VERDAD SENTI QUE EL 1 Y 2 SON LO MISMO SOLO CON DIFERENTE FORMA DE PEDIRLO
alien = 'verde','amarillo','rojo'
if 'verde' in alien:
    print(Fore.LIGHTGREEN_EX+"Felicidades!! Tienes 5 Puntos"+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+"No tienes 5 Puntos"+Style.RESET_ALL)
alien = 'amarillo','rojo'
if 'verde' in alien:
    print(Fore.LIGHTGREEN_EX+"Felicidades!! Tienes 5 Puntos"+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+"No tienes 5 Puntos"+Style.RESET_ALL)

print("")
print(Fore.LIGHTCYAN_EX+"3:"+Style.RESET_ALL)
aliencito = 'verde', 'amarillo', 'rojo'

if 'verde' in aliencito:
    print(Fore.LIGHTGREEN_EX+"Felicidades!! Tienes 5 Puntos"+Style.RESET_ALL)
elif 'amarillo' in aliencito:
    print(Fore.LIGHTYELLOW_EX+"Felicidades!! Tienes 10 Puntos"+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+"Felicidades!! Tienes 15 Puntos"+Style.RESET_ALL)

aliencito =  'amarillo', 'rojo'
if 'verde' in aliencito:
    print(Fore.LIGHTGREEN_EX+"Felicidades!! Tienes 5 Puntos"+Style.RESET_ALL)
elif 'amarillo' in aliencito:
    print(Fore.LIGHTYELLOW_EX+"Felicidades!! Tienes 10 Puntos"+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+"Felicidades!! Tienes 15 Puntos"+Style.RESET_ALL)    
aliencito = 'rojo'
if 'verde' in aliencito:
    print(Fore.LIGHTGREEN_EX+"Felicidades!! Tienes 5 Puntos"+Style.RESET_ALL)
elif 'amarillo' in aliencito:
    print(Fore.LIGHTYELLOW_EX+"Felicidades!! Tienes 10 Puntos"+Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX+"Felicidades!! Tienes 15 Puntos"+Style.RESET_ALL)    
print("")
print(Fore.LIGHTCYAN_EX+"4:"+Style.RESET_ALL)
edad = 1
if edad < 2:
    print(Fore.BLUE+"¡Es un bebé!")
elif edad < 4:
    print(Fore.MAGENTA+"¡Es un niño pequeño!")
elif edad < 13:
    print(Fore.GREEN+"¡Es un niño!")
elif edad < 20:
    print(Fore.YELLOW+"¡Es un adolescente!")
elif edad < 65:
    print(Fore.RED+"¡Es un adulto!")
else:
    print(Fore.CYAN+"¡Es un anciano!")

edad = 3
if edad < 2:
    print(Fore.BLUE+"¡Es un bebé!")
elif edad < 4:
    print(Fore.MAGENTA+"¡Es un niño pequeño!")
elif edad < 13:
    print(Fore.GREEN+"¡Es un niño!")
elif edad < 20:
    print(Fore.YELLOW+"¡Es un adolescente!")
elif edad < 65:
    print(Fore.RED+"¡Es un adulto!")
else:
    print(Fore.CYAN+"¡Es un anciano!")

edad = 5
if edad < 2:
    print(Fore.BLUE+"¡Es un bebé!")
elif edad < 4:
    print(Fore.MAGENTA+"¡Es un niño pequeño!")
elif edad < 13:
    print(Fore.GREEN+"¡Es un niño!")
elif edad < 20:
    print(Fore.YELLOW+"¡Es un adolescente!")
elif edad < 65:
    print(Fore.RED+"¡Es un adulto!")
else:
    print(Fore.CYAN+"¡Es un anciano!")

edad = 17
if edad < 2:
    print(Fore.BLUE+"¡Es un bebé!")
elif edad < 4:
    print(Fore.MAGENTA+"¡Es un niño pequeño!")
elif edad < 13:
    print(Fore.GREEN+"¡Es un niño!")
elif edad < 20:
    print(Fore.YELLOW+"¡Es un adolescente!")
elif edad < 65:
    print(Fore.RED+"¡Es un adulto!")
else:
    print(Fore.CYAN+"¡Es un anciano!")

edad = 30
if edad < 2:
    print(Fore.BLUE+"¡Es un bebé!")
elif edad < 4:
    print(Fore.MAGENTA+"¡Es un niño pequeño!")
elif edad < 13:
    print(Fore.GREEN+"¡Es un niño!")
elif edad < 20:
    print(Fore.YELLOW+"¡Es un adolescente!")
elif edad < 65:
    print(Fore.RED+"¡Es un adulto!")
else:
    print(Fore.CYAN+"¡Es un anciano!")

edad = 70
if edad < 2:
    print(Fore.BLUE+"¡Es un bebé!")
elif edad < 4:
    print(Fore.MAGENTA+"¡Es un niño pequeño!")
elif edad < 13:
    print(Fore.GREEN+"¡Es un niño!")
elif edad < 20:
    print(Fore.YELLOW+"¡Es un adolescente!")
elif edad < 65:
    print(Fore.RED+"¡Es un adulto!")
else:
    print(Fore.CYAN+"¡Es un anciano!")

print("")
print(Fore.LIGHTCYAN_EX+"5:"+Style.RESET_ALL)
favority_food =['manzana','uva','fresa']
if 'manzana' in favority_food:
    print(Fore.LIGHTGREEN_EX+"¡Realmente te gustan las manzanas!")
if 'uva' in favority_food:
    print(Fore.LIGHTYELLOW_EX+"¡Realmente te gustan las uvas!")
if 'fresa' in favority_food:    
    print(Fore.LIGHTRED_EX+"¡Realmente te gustan las fresas!"+Style.RESET_ALL)
if 'pera' in favority_food:
    print(Fore.MAGENTA+"¡Realmente te gustan las peras!")
if 'sandia' in favority_food:
    print(Fore.BLUE+"¡Realmente te gustan las sandías!")

"""
 EJERCICIOS
    1. Hola Administrador: Haz una lista de cinco o más nombres de usuario, 
    incluyendo el nombre 'admin'. Imagina que estás escribiendo un código 
    que imprimirá un saludo a cada usuario después de que inicien sesión en un
    sitio web. Recorre la lista e imprime un saludo para cada usuario:

        -Si el nombre de usuario es 'admin', imprime un saludo especial, como:
            "Hola admin, ¿te gustaría ver un informe de estado?" 
        De lo contrario, imprime un saludo genérico, como: 
            "Hola Eric, gracias por iniciar sesión nuevamente."

    2. Sin Usuarios: Agrega una prueba if para asegurarte de que la lista de
    usuarios no esté vacía.

        - Si la lista está vacía, imprime el mensaje 
            "¡Necesitamos encontrar algunos usuarios!".
        - Elimina todos los nombres de usuario de tu lista y asegúrate de que
            se imprima el mensaje correcto.
 
    3. Comprobando Nombres de Usuario: Haz lo siguiente para crear un programa
    que simule cómo los sitios web aseguran que cada usuario tenga un nombre
    único.

        - Crea una lista de cinco o más nombres de usuario llamada 
            usuarios_actuales.
        - Crea otra lista de cinco nombres de usuario llamada nuevos_usuarios.
            Asegúrate de que uno o dos de los nuevos nombres de usuario 
            también estén en la lista de usuarios_actuales.
        - Recorre la lista de nuevos_usuarios para ver si cada nuevo nombre
            de usuario ya ha sido usado. Si ya ha sido usado, imprime un 
            mensaje indicando que la persona deberá ingresar un nuevo nombre
            de usuario. Si un nombre de usuario no ha sido usado, imprime 
            un mensaje diciendo que el nombre de usuario está disponible.
        - Asegúrate de que la comparación sea insensible a mayúsculas. 
            Si se ha usado 'Juan', no se debe aceptar 'JUAN'.

"""

print("")
print(Fore.LIGHTCYAN_EX+"--------------Tercer Tomo de ejercicios-------------".title()+Style.RESET_ALL)
print("")
print(Fore.LIGHTCYAN_EX+"1:"+Style.RESET_ALL)
Lista_Nombres =['admin','yepez','ricardo','josue','felipa','brandon','nahim']
for nombresss in Lista_Nombres:
    if 'admin' == nombresss:
        print(Fore.LIGHTBLUE_EX+f"Hola {Fore.LIGHTMAGENTA_EX+nombresss.title()+Style.RESET_ALL}, "+Fore.LIGHTBLUE_EX+"¿Te gustaria ver un informe de estado?"+Style.RESET_ALL)
    else:
        print(Fore.LIGHTGREEN_EX+f"Hola {Fore.LIGHTMAGENTA_EX+nombresss.title()+Style.RESET_ALL}, "+Fore.LIGHTGREEN_EX+"Gracias por iniciar sesion nuevamente."+Style.RESET_ALL)
    


"""

    Ejercicios.

        1. Persona: Usa un diccionario para almacenar información sobre una 
            persona que conoces. Guarda su nombre, apellido, edad y la ciudad
            en la que vive. Deberías tener claves como nombre, apellido, edad y 
            ciudad. Imprime cada pieza de información almacenada en tu 
            diccionario.

        2. Números Favoritos: Usa un diccionario para almacenar los números 
            favoritos de varias personas. Piensa en cinco nombres y úsalos como
            claves en tu diccionario. Piensa en un número favorito para cada 
            persona y guárdalo como valor en tu diccionario. Imprime el nombre de
            cada persona y su número favorito. Para hacerlo más divertido, 
            encuesta a algunos amigos y obtén datos reales para tu programa.

        3. Glosario: Un diccionario de Python puede usarse para modelar un 
        diccionario real. Sin embargo, para evitar confusiones, llamémoslo 
        glosario.

            - Piensa en cinco palabras de programación que hayas aprendido en los 
            capítulos anteriores. Usa estas palabras como claves en tu glosario y
            guarda sus significados como valores.

            - Imprime cada palabra y su significado en una salida bien formateada. 
            Podrías imprimir la palabra seguida de dos puntos y luego su 
            significado, o imprimir la palabra en una línea y su significado 
            indentado en una segunda línea. Usa el carácter de nueva línea (\n) 
            para insertar una línea en blanco entre cada par palabra-significado
            en tu salida.

"""

"""
    Ejercicios:
    
        1. Glosario 2: Ahora que sabes cómo recorrer un diccionario con un 
            bucle, modifica el código del ejercicio anterior reemplazando tu 
            serie de instrucciones print con un bucle que recorra las claves y
            valores del diccionario. Cuando estés seguro de que tu bucle 
            funciona, agrega cinco términos más de Python a tu glosario. Al 
            ejecutar el programa nuevamente, estas nuevas palabras y sus 
            significados deberían incluirse automáticamente en la salida.

        2. Ríos: Crea un diccionario que contenga tres ríos importantes y el 
        país por el que cada río fluye. Un par clave-valor podría ser 
        'nilo': 'egipto'.

            - Usa un bucle para imprimir una oración sobre cada río, como: El Nilo fluye por Egipto.
            - Usa un bucle para imprimir el nombre de cada río incluido en el diccionario.
            - Usa un bucle para imprimir el nombre de cada país incluido en el diccionario.

"""
from colorama import Fore, Style

# Inicializar Colorama
import colorama
import pyfiglet
colorama.init()
import requests
"""

"""
covenat_1 = {'color': 'blue','points': 10}
print(covenat_1['color'])
print(covenat_1['points'])

covenat_1["x-position"] = 0
covenat_1["y-position"] = 25    
print(covenat_1)
print(Fore.LIGHTCYAN_EX+"\n"+"-------------Clase Dia 25/10/2024---------------"+Style.RESET_ALL)
programing_lenguages = {
    'alan': 'python',
    'valente': 'c++',
    'ariel': 'c',
    'yepez': 'java',
}
print(programing_lenguages['valente'].title())

for Nombre, Lenguage in programing_lenguages.items():
    print(f"A {Nombre.title()} Le gusta el lenguaje {Lenguage}")
print("")    
"""
   keys
"""

friends = ['ariel','yepez']
for name in programing_lenguages.keys():
    if name in friends:
        print(f"{name.title()}, Hola es un gusto saber que te gusta: {programing_lenguages[name]}")

if 'charly' not in programing_lenguages.keys():
    print("A charly no le gusta programar")
print("")
print(programing_lenguages.keys())

for key in sorted(programing_lenguages.keys()):
    print(key)
print("")
for key in (programing_lenguages.keys()):
    
    print(key)
print('\n')
for lenguajes in programing_lenguages.values():
    print(lenguajes)
for lenguajes in set(programing_lenguages.values()):
    print(lenguajes)
## El set elimina los elementos de ua lista repetido
print(Fore.LIGHTCYAN_EX+"\n"+"-------------Clase Dia 28/10/2024---------------"+Style.RESET_ALL+"\n")
"""
   Nesting
"""
covenant_elite= {'Color':'Blue','puntos': 10}
covenant_jackals = {'color':'gray','puntos': 8}
covenant_grunt = {'color': 'orange','punntos': 5}

covenants = [covenant_elite,covenant_jackals,covenant_grunt]
print("---------Covenants--------- ")
print(covenants)

for covenaassa in covenants:
    print(covenaassa)

## Vamos a crear una flotilal de 30 covenants grups
covenant_fleet = []
for covenanaaaa in range(30):
    new_covenantt = {'color':'orange','puntos': 5}
    covenant_fleet.append(new_covenantt)
print(covenant_fleet)
print("----Len----")
print(len(covenant_fleet)) ## El len se  usa para saber cuantos elementos hay en una lista
print(Fore.LIGHTCYAN_EX+"\n"+"-------------Clase Dia 29/10/2024---------------"+Style.RESET_ALL)

"""
Diccionarios en lista
listas en diccionarios
diccionarios en diccionarios
"""

##Dicionarios en lista
tacos = {
    "tortillas":['harina','maiz'],
    "Guisos":['bistek','tripa','pastor'],
}
print(f"Charly quiere unos tacos de {tacos['Guisos'][0]} en tortilla de {tacos['tortillas'][0]}".title())

## IMPRIMIR LOS LENGUAJES DE CADA PERSONA
favorite_games = {
    'charly':['fornite','halo','gears of wars'],
    'alan':['apex','warzone','conter'],
    'valente':['minecraft','rocketleague','blasphemous'],
    'doria':['valorant','blackops']
}
for name, games in favorite_games.items():
    print(name)
    for game in games:
        print("\t"+game.title())
"""
   Diccionarios en diccionarios
"""




####
##El siguiente tema no lo entendi
####

#caso de uso user names en una aplicación web
users = {
    "Charlymercury":{
        "firstname":"Carlos ",
        "lastname":"Tovar",
        "age": 32,
        "height":175,
    }
}
for user, user_info in users.items():
    print(user)
    full_name = user_info['firstname']+ user_info['lastname']
    print(full_name, "tiene: " f"{(user_info)['age']} años", f"Y mide: {(user_info)['height']}")
    
print(Fore.LIGHTCYAN_EX+"----------Trabajos dia 31/10/2024------------"+Style.RESET_ALL+"\n")
api_url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=151"
responde = requests.get(api_url)
responder = responde.json()
pokemons = responder['results']
for pokemon in pokemons:
    print(Fore.LIGHTGREEN_EX + f"Pokemon: "+Style.RESET_ALL+ f"{pokemon['name']}".title())  
    print(Fore.LIGHTMAGENTA_EX + f"Disponible en: "+Style.RESET_ALL + Fore.LIGHTBLUE_EX + f"{pokemon['url']}"+Style.RESET_ALL)

## Listas en diccionarios
##diccionarios en diccionarios

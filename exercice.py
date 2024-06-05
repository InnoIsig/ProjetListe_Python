#les modules
def addition(a, b):
    return a + b

if __name__ == "__main__":
    print(addition(4, 5)) 

import sys

from pprint import pprint
pprint(sys.path)

#les anotations
def add(a: int, b: int) -> int:
    return a + b

add(1, 3)

#affichage fonction multiple
def list(*list_item):
    for item in list_item:
        print(item)
list("epee")
list("Soupe", "Pima", "tomate", "Gout")

#Difference entre le plus grand nombre et le plus petit

def la_difference(nombre1, nombre2):
    if nombre1 > nombre2:
        return nombre1
    elif nombre1 < nombre2:
        return nombre2
    else:
        return "C'est l'égalité"
    
print(la_difference(4, 4))
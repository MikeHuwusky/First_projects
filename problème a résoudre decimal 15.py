from decimal import *
getcontext().prec = 20
import math
def racine(a):
    return math.sqrt(a)

nombre=6
continuer="o"

while continuer == "o":
    nombre = racine(nombre)
    print(nombre)
    continuer = input("voulez vous continuer (o/n)")

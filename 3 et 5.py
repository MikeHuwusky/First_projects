liste = []
for nombre in range(1000):
    if nombre % 3 == 0:
        liste.append(nombre)
    elif nombre % 5 == 0:
        liste.append(nombre)

resultat = 0
for chiffres in liste:
    resultat = chiffres + resultat

print(resultat)
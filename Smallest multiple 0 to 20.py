x = 0
liste = []
z = 1 
resultat = 0

for y in range(1000):
    if resultat > 1:
        resultat = x + y
        print(resultat)
        if resultat % z == 0:
                liste.append(resultat)


print(liste)
def conj(nombre):
    while nombre != 1:
        if nombre <= 1:
            print('terminer {nombre}')
        if nombre % 2 == 0:
            nombre = nombre // 2
            print(nombre)
        else:
            nombre = nombre * 3 + 1
            print(nombre)

chiffre = 1
liste = []

while chiffre < 10000:
    conj(chiffre)
    liste.append(chiffre)
    chiffre += 1

somme = 0

for nombre in liste:
    somme = somme + nombre

print(somme)
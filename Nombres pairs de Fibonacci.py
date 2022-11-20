
a = 1
b = 2
c = 0
resultat = 0
resultat1 = 0
liste = [1, 2]
liste1 = []

while resultat <4000000:
    if resultat <4000000:
        c = a + b
        liste.append(c)
        print(c)
        resultat = c
        if resultat <4000000:
            a = b + c
            liste.append(a)
            print(a)
            resultat = a
            if resultat <4000000:
                b = c + a
                liste.append(b)
                print(b)
                resultat = b
            else:
                resultat = 4000000
                liste.pop(-1)
        else:
            resultat = 4000000
            liste.pop(-1)
    else:
        resultat = 4000000
        liste.pop(-1)

for paire in liste:
    if paire % 2 == 0:
        liste1.append(paire)

for nombre in liste1:
    resultat1 = resultat1 + nombre
    print(resultat1)

print(resultat1)
nombre = int(input('Entrez un nombre entier : '))
liste = []
listef = []

for x in range(1, nombre):
    r = nombre / x
    g = nombre / r
    if g.is_integer():
        liste.append(format(float(r), ".4f"))

for t in liste:
    f = float(t)
    if f.is_integer():
        i = int(f)
        listef.append(i)
    else:
        listef.append(f)
    
print(f'les diviseur de {nombre} sont :')
for terms in range(len(liste)):
    print(listef[terms])

input('Appuyer ENTER pour quitter')
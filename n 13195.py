n = 600851475143 
liste = []
listel = []
rl = 1

for x in range(1, n):
    re = n / x
    if re.is_integer():
        liste.append(int(re))
        

liste.reverse()
print(liste)
for o in liste:
    rl = rl * o
    print(o)
    if rl == n:
        print(rl)
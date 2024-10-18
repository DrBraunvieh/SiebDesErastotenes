import math

zahlenListe = []

def sieb(liste, n):
    i = 2
    while(i <= math.ceil(math.sqrt(n))):
        for x in liste:
            if x % i == 0:
                liste.remove(x)
        print(liste)
        i = i +1

def füllListe(m):
    i = 1
    while(i<=m):
        zahlenListe.append(i)
        i = i + 1

n = int(input("How many numbers shall the List contain?"))
füllListe(n)
print(zahlenListe)
sieb(zahlenListe, n)
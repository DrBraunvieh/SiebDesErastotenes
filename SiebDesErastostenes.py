import math

zahlenListe = []

def sieb(liste, n):
    i = 2
    while(i <= math.ceil(math.sqrt(n))):
        faktor = 2
        for x in liste:
            if (faktor * x) % i == 0:
                liste.remove(x)
        faktor = faktor + 1
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
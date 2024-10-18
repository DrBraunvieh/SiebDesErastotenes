import math

zahlenListe = []
primzahlen = []

def siebRichtig(liste):
    grenze = int(math.sqrt(len(liste)))
    zahl = 2

    while(zahl <= grenze):
        faktor = 2

        while(faktor*zahl < len(liste)):
            liste.remove(faktor*zahl)
            faktor = faktor + 1
        zahl = zahl + 1
    return liste

def füllListe(m):
    i = 1
    while(i<=m):
        zahlenListe.append(i)
        i = i + 1

n = int(input("How many numbers shall the List contain?"))
füllListe(n)
primzahlen = siebRichtig(zahlenListe)
print(primzahlen)
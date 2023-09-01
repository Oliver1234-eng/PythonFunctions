### Zadatak 2. Napiši program koji za zadati niz brojeva:
### · Ispisuje najmanji element niza
### · Ispisuje najveći element niza
### · Ispisuje sumu vrednosti u nizu
### · Ispisuje srednju vrednost za niz
### Svaki od zadatih zahteva trebada bude implementiran kao posebna funkcija.
### Primer izvršavanja programa:
### >>> karakteristikeNiza([1,2,3,4,5,-1,6])
### Najmanji element niza je: -1
### Najveci element niza je: 6
### Suma elemenata niza je: 20
### Prosek elemenata niza je: 2.857142857142857
def min_niza(niz):
    return min(niz)

def max_niza(niz):
    return max(niz)

def suma_niza(niz):
    return sum(niz)

def srednja_vrednost_niza(niz):
    return sum(niz) / len(niz)

def karakteristikeNiza(niz):
    print("Najmanji element niza je:", min_niza(niz))
    print("Najveci element niza je:", max_niza(niz))
    print("Suma elemenata niza je:", suma_niza(niz))
    print("Prosek elemenata niza je:", srednja_vrednost_niza(niz))

# primer izvršavanja programa
karakteristikeNiza([1,2,3,4,5,-1,6])
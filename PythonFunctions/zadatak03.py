### Zadatak 3. Napiši funkciju koja čita iz fajla korisnička imena i lozinke i pročitane vrednosti vraća kao
### listu. Prilikom poziva funkcije prosleđuje se naziv fajla i delimiter kojim je u fajlu korisničko ime odvojeno
### od lozinke. Pri tome je element liste koja se vraća lista u kojoj je prvi element korisničko ime, a drugi element lozinka.
### Primer izvršavanja programa:
### Za fajl korisnici.txt
### pera|peric
### jova|jovic
### steva|stevic
### rezultat poziva funkcije treba da bude:
### >>> print(citanjeIzFajla("korisnici.txt","|"))
### [['pera', 'peric'], ['jova', 'jovic'], ['steva', 'stevic']]
def citanjeIzFajla(naziv_fajla, delimiter):
    korisnici = []
    with open(naziv_fajla, "r") as f:
        for linija in f:
            ime, lozinka = linija.strip().split(delimiter)
            korisnici.append([ime, lozinka])
    return korisnici

print(citanjeIzFajla("korisnici.txt", "|"))
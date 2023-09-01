### Zadatak 4. Napiši funkciju za registrovanje korisnika. Funkcija prima korisničko ime, lozinku, naziv fajla u
### koji se snima i delimiter kojim će biti razdvojeno korisničko ime i lozinka. Korisničko ime i lozinku se
### snimaju u fajl sa zadatim nazivom. Ta funkcija vraća korisnička imena i lozinke svih registrovanih
### korisnika, kao što je specificirano u zadatku 3.
### Primer izvršavanja programa:
### Za fajl korisnicidva.txt
### pera|peric
### jova|jovic
### steva|stevic
### rezultat poziva funkcije treba da bude:
### >>> print(upisUFajl("marko","markovic","korisnici.txt","|"))
### [['pera', 'peric'], ['jova', 'jovic'], ['steva', 'stevic'], ['marko', 'markovic']]
### fajl korisnicidva.txt nakon navedenog izvršavanja programa treba da sadrži:
### pera|peric
### jova|jovic
### steva|stevic
### marko|markovic
def citanjeIzFajla(naziv_fajla, delimiter):
    with open(naziv_fajla, "r") as f:
        linije = f.readlines()
        korisnici = [linija.strip().split(delimiter) for linija in linije]
        return korisnici

def upisUFajl(korisnicko_ime, lozinka, naziv_fajla, delimiter):
    with open(naziv_fajla, "a") as f:
        f.write(korisnicko_ime + delimiter + lozinka + '\n')
    return citanjeIzFajla(naziv_fajla, delimiter)

print(upisUFajl("marko", "markovic", "korisnicidva.txt", "|"))
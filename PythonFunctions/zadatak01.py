### Zadatak 1. Kvadratna jednačina zadata je formatom ax2 + bx + c = 0. Koreni kvadratne jednačine
### računaju se kao x1,2 = (-b +- sqrt(b2 - 4ac)) / 2a. Napisati funkciju koja prima parametre a,b i c i vraća rešenja kvadratne jednačine. Pri tome se pretpostavlja da postoje realni koreni kvadratne jednačine.
### Primer izvršavanja programa:
### >>> print(kvJednacina(-1,5,5))
### (-0.8541019662496847, 5.854101966249685)
import math

def kvJednacina(a, b, c):
    # izračunaj diskriminantu
    D = b**2 - 4*a*c
    
    # izračunaj korene kvadratne jednačine
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    
    return (x1, x2)

print(kvJednacina(-1, 5, 5))

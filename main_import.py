from osoba import Osoba
from zamestnanec import *
#import osoba
from matematicke_funkce import *
import math
import random as rd

zdenek = Osoba("Zdenek", 78)
print(zdenek)

kveta = Zamestanec("Kveta", 50, 40000)
kveta.predstav_se()


cisla = [10, 7, 5, 3, 8, 2000]

print("median: {:.2f}".format(spocitej_median(cisla)))
print("prumer: {:.2f}".format(spocitej_prumer(cisla)))

zaklad = 0.1247
exponent = 0.478
print("Mocnina operator: {}.".format(zaklad**exponent))
print("Defaultni pow: {}.".format(pow(zaklad,exponent)))
print("Math power: {}.".format(math.pow(zaklad,exponent)))

nahodne_cislo = rd.randint(0,1)
print(nahodne_cislo)

vylosovane_cislo = rd.choice(cisla)
print(vylosovane_cislo)

vylosovane_pismeno = rd.choice("Hello Word")
print(vylosovane_pismeno)

marek = Manazer("Marek", 13, 700000)
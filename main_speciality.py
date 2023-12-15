from matematicke_funkce import *

cislo = 10
cislo1 = 33

print("cislo: " + str(cislo))
print("cislo1: " + str(cislo1))

cislo1, cislo = cislo, cislo1

print("po prohozeni")
print("cislo: " + str(cislo))
print("cislo1: " + str(cislo1))

jmeno, vek, plat = ["Pepa", 20, 50000]
print("jmeno: " + jmeno)
print("vek: " + str(vek))
print("plat: " + str(plat))

jmeno, *ostatni = ["Pepa", 20, 50000]
print("jmeno: " + jmeno)
print("ostatni: " + str(ostatni))
print("typ ostatni: " + str(type(ostatni)))

def secti_a_vynasob(nasobitel,*scitanci):
    soucet = 0
    for cislo in scitanci:
        soucet += cislo
    print(locals())
    return soucet * nasobitel

print("secti a vynasob: " + str(secti_a_vynasob(10, 4, 2, 3)))

text = "Moje jmeno je {} a je mi {} let.".format("Petr", 37)
print(text)

text1 = "Moje jmeno je {jmeno} a je mi {vek} let.".format(vek=37, jmeno="Petr")
print(text1)

text2 = "Moje jmeno je {1} a je mi {0} let.".format(37, "Petr")
print(text2)

formatovane_desetine_cislo = "{:.2f}".format(10/3)
print(formatovane_desetine_cislo)

cislo = 10
print("Je cislo integer: {}".format(isinstance(cislo,int)))
print("Je cislo integer: {}".format(isinstance(cislo,str)))

ovoce = ["jablko", "meloun", "hruska", "tresen"]
ovoce_obsahuje_a = []

for jedno_ovoce in ovoce:
    if "a" in jedno_ovoce:
        ovoce_obsahuje_a.append(jedno_ovoce)

print("ovoce: {}".format(ovoce))
print("ovoce_obsahuje_a: {}".format(ovoce_obsahuje_a))

#ovoce_obsahuje_a = [x for x in ovoce if "a" in x]
ovoce_obsahuje_a = [jedno_ovoce for jedno_ovoce in ovoce if "a" in jedno_ovoce]

print("ovoce: {}".format(ovoce))
print("ovoce_obsahuje_a: {}".format(ovoce_obsahuje_a))

def proved_vypocet(funkce, cisla):
    return funkce(cisla)

moje_cisla = [12, 7, 7, 8, 15, 200]

print("Proved vypocet medianu: {:.2f}".format(proved_vypocet(spocitej_median, moje_cisla)))
print("Proved vypocet prumer: {:.2f}".format(proved_vypocet(spocitej_prumer, moje_cisla)))

seznam = []

if(seznam):
    print("seznam neni prazdny")
else:
    print("seznam je prazdny")

seznam.append("hello")
print("po pridani")
if (seznam):
    print("seznam neni prazdny")
else:
    print("seznam je prazdny")

print(*moje_cisla)


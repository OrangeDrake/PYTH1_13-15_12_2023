
delenec = 10
delitel = 3

vysledek = delenec /delitel
print(vysledek)

delenec /= delitel
print(delenec)

delenec = 10
delitel = 3

zbytek = delenec % delitel
print(zbytek)

delenec %= delitel
print(delenec)

cislo = 100
cislo1 = 130
cislo2 = 100

if cislo == cislo1:
    print("Cisla jsou rovna")

if cislo != cislo1:
    print("Cisla nejsou rovna")

jsouRovna = cislo == cislo1
print(jsouRovna)
print(type(jsouRovna))

if cislo == cislo1 and cislo1 == cislo2:
    print("cislo je rovno cislo2")
else:
    print("cislo nemusi byt rovno cislo2")

zaklad = 2
exponent = 3

mocnina = zaklad**exponent
print("mocnina: " + str(mocnina))




delenec = 10
delitel = 3

try:
    vysledek = delenec / delitel
    print("vysledek: " + str(vysledek))
except ZeroDivisionError:
    print("Nelze delit nulou")

while True:
    try:
        cele_cislo = int(input("zadej cele cislo: "))
        print("zadane cele cislo: " + str(cele_cislo))
        break
    except ValueError:
        print("nebylo zadano cele cislo")

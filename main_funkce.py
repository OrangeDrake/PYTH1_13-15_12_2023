def pridej_do_seznamu(seznam, prvek):
    seznam.append(prvek)

def secti(scitanec, scitanec1):
    vysledek_scitani = scitanec + scitanec1
    return vysledek_scitani



moje_cisla = [1, 3, -5]
pridej_do_seznamu(moje_cisla, 8)
print("cisla: " + str(moje_cisla))

pridej_do_seznamu(moje_cisla, "hello")
print(moje_cisla)

vysledek = secti(4, 7)
print(vysledek)

# vysledek = secti("hello ", "word")
# print(vysledek  )


#Nepouzivat kombinaci lokalnich a globalnich promennych
seznam = [0, 0, 0,]
cisla1 = [0, 0, 0,]
moje_cisla = [1, 4, 10]

def pridej_do_seznamu_dvakrat(seznam, seznam1, prvek):
    seznam.append(prvek)
    seznam1.append(prvek)
    cisla1.append(prvek)

pridej_do_seznamu_dvakrat(moje_cisla, moje_cisla, 10)
print("moje_cisla: " + str(moje_cisla))
print("seznam: " + str(seznam))
print("cisla1: " + str(cisla1))


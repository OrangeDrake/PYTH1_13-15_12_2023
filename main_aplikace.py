def pridej_cislo(cisla, cislo):
    cisla.append(cislo)

def vypis_cisla(cisla):
    print(cisla)

def zadani_cisla():
    while True:
        try:
            zvolene_cislo = int(input("zadej cislo:"))
            return zvolene_cislo
        except ValueError:
            print("nebylo zadano cele cislo")

def zadani_cisla_s_maximalnim_poctem_zadani(maximalni_pocet_zadani):
    pocet_zadani = 0
    while True:
        if pocet_zadani == maximalni_pocet_zadani:
            return None
        try:
            zvolene_cislo = int(input("zadej cislo:"))
            return zvolene_cislo
        except ValueError:
            pocet_zadani += 1
            print("nebylo zadano cele cislo")

def odeber_cislo(cisla, cislo):
    try:
        cisla.remove(cislo)
        return True
    except ValueError:
        return False

def odeber_cislo2(cisla, cislo):
    if cislo not in cisla:
        return False
    cisla.remove(cislo)
    return True

def spocitej_prumer(cisla):
    soucet = 0
    for cislo in cisla:
        soucet += cislo
    return soucet / len(cisla)

def spocitej_median(cisla):
    kopie_cisla = cisla[:]
    kopie_cisla.sort()

    delka_seznam = len(kopie_cisla)

    if (delka_seznam % 2 == 1 ):
        return kopie_cisla[delka_seznam//2]
    return (kopie_cisla[delka_seznam//2 -1] + kopie_cisla[delka_seznam//2])/2



ulozena_cisla = []

while True:
    print("----------------")
    volba = input("[1] pridej cislo, [2] zobrazit cisla, [3] odeber cislo, [4] spocitej prumer, [5] spocitej median, [konec] konec aplikace : ")
    if (volba == "1"):
        #zvolene_cislo = zadani_cisla()
        zvolene_cislo = zadani_cisla_s_maximalnim_poctem_zadani(3)
        if (zvolene_cislo == None):
            print("cislo nebylo pridano")
            continue
        pridej_cislo(ulozena_cisla, zvolene_cislo)
        print("cislo bylo pridano")
    elif (volba == "2"):
        vypis_cisla(ulozena_cisla)
    elif (volba == "3"):
        zvolene_cislo = zadani_cisla_s_maximalnim_poctem_zadani(3)
        if (zvolene_cislo == None):
            print("cislo nebylo odebrano, chybne zadani cislo")
            continue
        # if not odeber_cislo(ulozena_cisla, zvolene_cislo):
        if not odeber_cislo2(ulozena_cisla, zvolene_cislo):
            print("cislo nebylo odebrano, cislo neni v seznamu")
            continue
        print("cislo bylo odebrano")
    elif (volba == "4"):
        prumer = spocitej_prumer(ulozena_cisla)
        print("prumer cisel je: " + str(prumer))
    elif(volba == "5"):
        median = spocitej_median(ulozena_cisla)
        print("median cisel je: " + str(median))
    elif (volba.lower() == "konec"):
        print("zaviram aplikaci")
        break
    else:
        print("neplatna volba")



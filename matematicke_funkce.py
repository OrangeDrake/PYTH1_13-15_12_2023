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

if __name__ == "__main__":
    cisla = [10, 7, 5, 3, 8, 2000]

    print("median z matematickych funkci: {:.2f}".format(spocitej_median(cisla)))
    print("prumer z matematickych funkci: {:.2f}".format(spocitej_prumer(cisla)))
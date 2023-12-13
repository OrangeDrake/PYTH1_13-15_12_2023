def vytvor_matici(pocet_radku, pocet_sloupcu):
    matice = []
    for i in range(pocet_radku):
        radek = []
        for i in range(pocet_sloupcu):
            radek.append(0)
        matice.append(radek)
    return matice

def vytvor_matici2(pocet_radku, pocet_sloupcu):
    matice = []
    for i in range(pocet_radku):
        radek = [0]*pocet_sloupcu
        matice.append(radek)
    return matice

def vypis_matici(matice):
    for radek in matice:
        for cislo in radek:
            print(cislo, end=" " )
        print()


# moje_matice = vytvor_matici(5,10)
moje_matice = vytvor_matici2(5,10)
vypis_matici(moje_matice)

moje_matice[1][9] = 9
print("po zmene")
vypis_matici(moje_matice)


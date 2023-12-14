from osoba import Osoba
from aplikace import zadani_cisla_s_maximalnim_poctem_zadani
class Sprava_osob:
    def __init__(self):
        self.osoby = []

    def pridej_osobu(self, osoba):
        self.osoby.append(osoba)

    def vytvor_osobu(self):
        jmeno = input("zadej jmeno osoby: ")
        print("zadej vek osoby.")
        vek = zadani_cisla_s_maximalnim_poctem_zadani(3)
        if vek == None:
            print("Vek nebyl zadan, osoba nebyla vytvorena")
            return None
        return Osoba(jmeno, vek)

    def uloz(self, nazev_souboru):
        with open(nazev_souboru, "w") as f:
            for osoba in self.osoby:
                f.write(osoba.jmeno + ";" + str(osoba.vek) + "\n")

    def nacti(self, nazev_souboru):
        try:
            with open(nazev_souboru, "r") as f:
                self.osoby.clear()
                for line in f:
                    if line == "\n":
                        continue
                    try:
                        jmeno, vek_text = line.split(";")
                        vek = int(vek_text)
                    except ValueError as e:
                        print(e)
                        print("Osoba nebyla nactena")
                        continue
                    osoba = Osoba(jmeno, vek)
                    self.osoby.append(osoba)
        except FileNotFoundError as e:
            print(e)
            print("data nebyla nactena")
            return False
        return True



    def spust(self):
        while True:
            print("--------------")
            volba = input("zadej volbu: [1] pridani osoby, [2] vypis osob, [3] uloz, [4] nacti, [konec] pro ukonceni aplikace: ").strip().lower()

            if (volba == "1"):
                osoba = self.vytvor_osobu()
                if osoba is None:
                    print("Osoba nebyla pridana")
                    continue
                self.pridej_osobu(osoba)

            elif (volba == "2"):
                if not self.osoby:
                    print("Database neobsahuje zadne osoby")
                    continue
                print("V databazi jsou ulozeny tyto osoby:")
                for osoba in self.osoby:
                    print(osoba)
            elif (volba == "3"):
                nazev_souboru = input("zadej nazev souboru: ")
                self.uloz(nazev_souboru)
                print("Stav aplikace byl ulozen do souboru:" + nazev_souboru)

            elif (volba == "4"):
                nazev_souboru = input("zadej nazev souboru: ")
                if not self.nacti(nazev_souboru):
                    print("Stav aplikace nebyl nahran ze souboru:" + nazev_souboru)
                    continue
                print("Stav aplikace byl nahran ze souboru:" + nazev_souboru)

            elif (volba == "konec"):
                print("Ukoncuji aplikaci")
                return

if __name__ == "__main__":
    sprava_osob = Sprava_osob()
    sprava_osob.spust()





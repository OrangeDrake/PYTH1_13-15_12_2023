from osoba import  Osoba
class Osoba_s_kamarady(Osoba):
    def __init__(self, jmeno, vek):
        super().__init__(jmeno, vek)
        self.kamaradi = []

    def pridej_kamarada(self, osoba_s_kamarady):
        self.kamaradi.append(osoba_s_kamarady)
        osoba_s_kamarady.kamaradi.append(self)
        print("{} pridal {} mezi sve kamarady".format(self.jmeno, osoba_s_kamarady.jmeno))
        print("Zaroven {1} pridal {0} mezi sve kamarady".format(self.jmeno, osoba_s_kamarady.jmeno))

    def odstan_kamarada_pomoci_poradi(self, poradi):
        pocet_kamaradu = len(self.kamaradi)
        if poradi < 1 or poradi > pocet_kamaradu:
            print("Neplatny index. {} se snazil odstanit {}. kamarada, pritom ma {} kamaradu.".format(self.jmeno, poradi, pocet_kamaradu))
            return
        index = poradi - 1
        odstanovana_osoba = self.kamaradi[index]
        self.kamaradi.pop(index)
        odstanovana_osoba.kamaradi.remove(self)
        print("{} odebral {} ze svych kamaradu".format(self.jmeno, odstanovana_osoba.jmeno))

    def predstav_se(self):
        super().predstav_se()
        if(not self.kamaradi):
            print("Nemam kamarady.")
            return
        print("Moji kamaradi jsou:", end=" ")
        pocet_kamaradu = len(self.kamaradi)
        for i in range(pocet_kamaradu):
            kamarad = self.kamaradi[i]
            if i < pocet_kamaradu - 1:
                print(str(i+1) + ": " + kamarad.jmeno, end=", ")
            else:
                print(str(i + 1) + ": " + kamarad.jmeno, end=". ")
        print()

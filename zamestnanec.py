from osoba import Osoba
class Zamestanec(Osoba):
    def __init__(self, jmeno, vek=0, plat=0):
        super().__init__(jmeno, vek)
        self.plat = plat

    def __str__(self):
        return "Zamestanec{jmeno:" + self.jmeno + ", vek:" + str(self.vek) + ", plat:" + str(self.plat) + "}"

    def pracuj(self):
        print("Zamestnanec " + self.jmeno + " tvori webovou aplikaci")

    def predstav_se(self):
         super().predstav_se()
         print("Muj plat je " + str(self.plat))

class Manazer(Zamestanec):
    def __init__(self, jmeno, vek, plat):
        super().__init__(jmeno, vek, plat)

    def pracuj(self):
        print("Manazer " + self.jmeno + " domlouva schuzky")
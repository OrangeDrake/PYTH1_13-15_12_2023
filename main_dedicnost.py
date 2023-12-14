class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return "Osoba{jmeno:" + self.jmeno + ", vek:" + str(self.vek) + "}"

    def __repr__(self):
        return self.jmeno

    def __eq__(self, other):
        return self.vek == other.vek

    def predstav_se(self):
        print("Jmenuji se " + self.jmeno + " a je mi " + str(self.vek))

class Zamestanec(Osoba):
    def __init__(self, jmeno, vek=0, plat=0):
        super().__init__(jmeno, vek)
        self.plat = plat

    def __str__(self):
        return "Zamestanec{jmeno:" + self.jmeno + ", vek:" + str(self.vek) + ", plat:" + str(self.plat) + "}"

    def pracuj(self):
        print("Zamestnanec " + self.jmeno + " tvori webovou aplikaci")

    def predstav_se(self):
        print("Jmenuji se " + self.jmeno + " a je mi " + str(self.vek) + ". Muj plat je " + str(self.plat))

class Manazer(Zamestanec):
    def __init__(self, jmeno, vek, plat):
        super().__init__(jmeno, vek, plat)

    def pracuj(self):
        print("Manazer " + self.jmeno + " domlouva schuzky")

jan = Zamestanec("Jan", 35, 40000)
jan.pracuj()
jan.predstav_se()
print("Plat Jana " + str(jan.plat))

milos = Osoba("Milos", 70)
milos.predstav_se()

petr = Zamestanec("Petr")
print(petr)

print(jan)

lubos = Manazer("Lubos", 45, 100000)
lubos.pracuj()
print("projiti listu")
zamestanci = [jan, lubos, milos]

for zamestnanec in zamestanci:
    if not isinstance(zamestnanec, Zamestanec):
        continue
    zamestnanec.pracuj()
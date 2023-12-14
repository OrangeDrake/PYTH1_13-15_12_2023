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
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


karel = Osoba("Karel", 20)
karel.predstav_se()
jiri = Osoba("Jiri", 40)
jiri.predstav_se()

print(karel)
print(jiri)

text = str(karel) + " a neco dalsiho"
print(text)

print("karel repr: " + repr(karel))
print("Jiri repr: " + repr(jiri))

print("Je Jiri stejne stary jako Karel: " + str(jiri == karel))

mirka = Osoba("Mirka", 40)
print("Je Mirka stejne stara jako Jiri: " + str(mirka == jiri))
print("Je Mirka stejny objekt jako Jiri: " + str(mirka is jiri))

fantom = jiri

print("Je Fantom stejny objekt jako Jiri: " + str(fantom is jiri))

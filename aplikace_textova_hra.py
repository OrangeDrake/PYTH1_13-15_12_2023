class Prikaz_jdi:
    nazev = "jdi"

    def __init__(self, herni_svet):
        self.herni_svet = herni_svet

    def proved(self, parametry):

        if not parametry:
            return "kam mam jit?"

        if parametry[0] == "napoveda":
            return self.zobraz_napovedu()

        smer = parametry[0]

        nova_lokalita = None
        if smer == "sever":
            if self.herni_svet.aktualni_lokalita.sever == None:
                return "na sever se neda jit"
            nova_lokalita = self.herni_svet.aktualni_lokalita.sever
        elif smer == "jih":
            if self.herni_svet.aktualni_lokalita.jih == None:
                return "na jih se neda jit"
            nova_lokalita = self.herni_svet.aktualni_lokalita.jih
        elif smer == "vychod":
            if self.herni_svet.aktualni_lokalita.vychod == None:
                return "na vychod se neda jit"
            nova_lokalita = self.herni_svet.aktualni_lokalita.vychod
        elif smer == "zapad":
            if self.herni_svet.aktualni_lokalita.zapad == None:
                return "na zapad se neda jit"
            nova_lokalita = self.herni_svet.aktualni_lokalita.zapad

        if nova_lokalita == None:
            return "Na " + smer + "se neda jit"

        self.herni_svet.aktualni_lokalita = nova_lokalita

        return "presunul jsi se " + nova_lokalita.jmeno

    def zobraz_napovedu(self):
        return "prikaz ma jeden parametr a to smer kam se ches posunout"

class Prikaz_pouzij:
    nazev = "pouzij"

    def proved(self, parametry):

        if not parametry:
            return "co mam pouzit?"

        if parametry[0] == "napoveda":
            return self.zobraz_napovedu()

        return "pouzil jsi " + parametry[0]

    def zobraz_napovedu(self):
        return "prikaz ma jeden parametr a to predmet, ktery chce pouzit"

class Prikaz_napoveda:
    nazev = "napoveda"

    def __init__(self, hra):
        self.hra = hra

    def proved(self, parametry):
        text = "Ve hre muzed pouzivat tyto prikazy:\n"
        for nazev_prikazu in hra.prikazy:
            prikaz = hra.prikazy[nazev_prikazu]
            text += prikaz.nazev + ": " + prikaz.zobraz_napovedu() + "\n"
        return text

    def zobraz_napovedu(self):
        return "prikaz ma nema parametr, vypise napovedu vsech prikazu"

class Herni_svet:

    def __init__(self):
        self.aktualni_lokalita = None
        self.sestav_svet()
    def sestav_svet(self):
        louka = Lokalita("Louka")
        hory = Lokalita("Hory")
        louka.sever = hory
        hory.jih = louka

        self.aktualni_lokalita = louka

class Lokalita:

    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.sever = None
        self.jih = None
        self.vychod = None
        self.zapad = None

class Hra:
    def __init__(self):
        self.prikazy = {}
        self.herni_svet = Herni_svet()
        self.zaregistruj_prikazy()


    def zaregistruj_prikazy(self):
        self.prikazy[Prikaz_jdi.nazev] = Prikaz_jdi(self.herni_svet)
        self.prikazy[Prikaz_pouzij.nazev] = Prikaz_pouzij()
        self.prikazy[Prikaz_napoveda.nazev] = Prikaz_napoveda(self)
    def spust(self):
        print(self.vrat_privitani())

        while True:
            prikaz, *parametry = input("Zadej prikaz: ").strip().split(" ")

            try:
                prikaz = self.prikazy[prikaz]
            except KeyError as e:
                print("Neplatni prikaz")
                continue
            odpoved = prikaz.proved(parametry)
            print(odpoved)

    def vrat_privitani(self):
        return "Vitej ve hre, muzes zadavat prikazy"


if __name__ == "__main__":
    hra = Hra()
    hra.spust()



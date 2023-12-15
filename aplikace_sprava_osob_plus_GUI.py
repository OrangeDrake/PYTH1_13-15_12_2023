from osoba import Osoba
from aplikace import zadani_cisla_s_maximalnim_poctem_zadani

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

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
        print("ve funkci nacti")
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

    def nacti_a_vyhodnot(self, nazev_souboru, label, okno):
        if not self.nacti(nazev_souboru):
            label.set("Soubor nenalezen, zadejte jiny nazez")
            return
        okno.destroy()

    def otevri_okno_nacteni(self, okno):
        nove_okno = Toplevel(okno)

        nacti_soubor_var = StringVar(nove_okno)
        nacti_soubor_entry = Entry(nove_okno, textvariable=nacti_soubor_var)

        nacti_soubor_entry.pack()
        nacti_soubor_button = Button(nove_okno, text ="nacti soubor", command=lambda: self.nacti_a_vyhodnot(nacti_soubor_entry.get(), info_var, nove_okno))

        info_var = StringVar()
        info_var.set("Zadejte nazev souboru")
        info_label = Label(nove_okno, textvariable=info_var)
        info_label.pack()

        nacti_soubor_button.pack()

    def nacteni_osob_popup (self, okno):
        path = filedialog.askopenfilename(title="Select a file", filetypes=(("text files", "*.txt"),
                                                                            ("all files", "*.*")))
        self.nacti(path)




    def otevri_okno_vypisu(self, okno):
        nove_okno = Toplevel(okno)
        vypis_text = Text(nove_okno)
        vypis_text.pack()
        vypis_text.config(state=NORMAL)
        vypis_text.delete(1.0, END)
        if not self.osoby:
            vypis_text.insert(END, "Nejsou zadne osoby")
        for osoby in self.osoby:
            vypis_text.insert(END, str(osoby) + "\n")
        vypis_text.config(state=DISABLED)



    def spust_GUI(self):
        root = Tk()
        root.title("Sprava osob")
        root.geometry("200x600")

        #otevri_okno_nacteni_button = Button(root, text = "Nacteni osob", command=lambda: self.otevri_okno_nacteni(root))
        otevri_okno_nacteni_button = Button(root, text="Nacteni osob", command=lambda: self.nacteni_osob_popup(root))
        otevri_okno_nacteni_button.pack()

        otevri_okno_vypisu_button = Button(root, text = "Vypis osob", command=lambda: self.otevri_okno_vypisu(root))
        otevri_okno_vypisu_button.pack()

        mainloop()



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
    #sprava_osob.spust()
    sprava_osob.spust_GUI()





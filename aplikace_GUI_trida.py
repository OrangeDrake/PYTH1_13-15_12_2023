from tkinter import *
from tkinter.ttk import *

class Kalkulacka:
    def __init__(self):
        self.root = Tk()
        self.cislo_variable = IntVar(self.root)
        self.cislo1_variable = IntVar(self.root)
        self.operator_variable = StringVar(self.root)
        self.vysledek_variable = IntVar(self.root)

    def vypocet(self):
        print("v metode vypocitej")
        try:
            cislo = self.cislo_variable.get()
            cislo1 = self.cislo1_variable.get()
        except TclError as e:
            self.cislo_variable.set(0)
            self.cislo1_variable.set(0)
            print(e)

        operator = self.operator_variable.get()

        vysledek = "---"
        if operator == "+":
            vysledek = cislo + cislo1
        elif operator == "-":
            vysledek = cislo - cislo1
        elif operator == "/":
            try:
                vysledek = cislo / cislo1
            except ZeroDivisionError as e:
                print(e)
                vysledek = "---"
        elif operator == "*":
            vysledek = cislo * cislo1
        else:
            self.operator_variable.set("")

        self.vysledek_variable.set(vysledek)

    def spust(self):
        self.root.title("Kalkulacka")
        self.root.geometry("1000x200")

        cislo_entry = Entry(self.root, textvariable=self.cislo_variable)
        cislo_entry.grid(row=0, column=0)
        operator_entry = Entry(self.root, textvariable=self.operator_variable)
        operator_entry.grid(row=0, column=1)
        cislo1_entry = Entry(self.root, textvariable=self.cislo1_variable)
        cislo1_entry.grid(row=0, column=2)

        rovnase_label = Label(self.root, text="=")
        rovnase_label.grid(row=0, column=3)

        vysledek_label = Label(self.root, textvariable=self.vysledek_variable)
        vysledek_label.grid(row=0, column=4)

        spocitej_button = Button(self.root, text="Vypocitej", command=self.vypocet)
        spocitej_button.grid(row=1, column=4)

        mainloop()

if __name__ == "__main__":
    kalkulacka = Kalkulacka()
    kalkulacka.spust()
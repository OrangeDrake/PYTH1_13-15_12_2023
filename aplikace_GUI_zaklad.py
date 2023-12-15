from tkinter import *
from tkinter.ttk import *

def vypis_hello():
    print("hello word")

def vypis_obsah_entry(text):
    print("bylo zadano: "+ text)

def pridej_do_seznamu(seznam, prvek):
    seznam.append(prvek)
    print(seznam)



seznam_textu = []

root = Tk()
root.title("Vzornik grafickych prvk")
root.geometry("400x700")

def pridej_do_seznamu_a_resetuj_variable(seznam, variable):
    prvek = variable.get()
    variable.set("")
    pridej_do_seznamu(seznam, prvek)

def ziskej_se_seznamu_a_zapis_do_text(seznam, text):
    text.config(state=NORMAL)
    text.delete(1.0, END)
    for prvek in seznam:
        text.insert(END, prvek + "\n")
    text.config(state=DISABLED)

def ziskej_se_seznamu_a_resetuj_a_zapis_do_text(seznam, text):
    ziskej_se_seznamu_a_zapis_do_text(seznam, text)
    seznam.clear()


hodnota_variable = StringVar(root, "sem neco zadajte")
pridej_do_seznamu_variable = StringVar(root)

nadpis_label = Label(root, text="Toto je uvodni aplikace")
nadpis_label.pack()

hodnota_entry = Entry(root, textvariable=hodnota_variable)
hodnota_entry.pack()

hodnota_label = Label(root, textvariable = hodnota_variable)
hodnota_label.pack()

ukazkove_button = Button(root, text ="Vypis hello", command=vypis_hello)
ukazkove_button.pack()

hodnota_tlacitko = Button(root, text ="Vypis text ve vstupu", command=lambda: vypis_obsah_entry(hodnota_variable.get()))
hodnota_tlacitko.pack()

pridej_do_seznamu_entry = Entry(root, textvariable=pridej_do_seznamu_variable)
pridej_do_seznamu_entry.pack()

pridej_do_seznamu_button = Button(root, text = "Pridej do seznamu", command = lambda: pridej_do_seznamu_a_resetuj_variable(seznam_textu, pridej_do_seznamu_variable))
pridej_do_seznamu_button.pack()

ziskej_se_seznamu_Text = Text(root)
ziskej_se_seznamu_Text.config(state=DISABLED)
ziskej_se_seznamu_Text.pack()

ziskej_seznamu_button = Button(root, text = "Zobraz seznam nahore", command= lambda:ziskej_se_seznamu_a_resetuj_a_zapis_do_text(seznam_textu, ziskej_se_seznamu_Text))
ziskej_seznamu_button.pack()

ziskej_seznamu_button1 = Button(root, text = "Zobraz seznam dole", command= lambda:ziskej_se_seznamu_a_resetuj_a_zapis_do_text(seznam_textu, ziskej_se_seznamu1_Text))
ziskej_seznamu_button1.pack()

ziskej_se_seznamu1_Text = Text(root)
ziskej_se_seznamu1_Text.config(state=DISABLED)
ziskej_se_seznamu1_Text.pack()



mainloop()

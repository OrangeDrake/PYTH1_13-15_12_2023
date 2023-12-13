print("hello")

cislo = 108
print(cislo)

print(type(cislo))

cislo = "word"
print(cislo)

print(type(cislo))

cislo = 100

print(cislo)
print(type((cislo)))

cislo1 = 10

vysledek = cislo / cislo1
print(vysledek)
print(type(vysledek))

vysledek = cislo // cislo1
print(vysledek)
print(type(vysledek))

text = "Hello Word"
cislo2 = 108
text_a_cislo = text + str(cislo2)
print(text_a_cislo)
print(type(text_a_cislo))

text_mala_pismena = text.lower()

print("text: " + text)
print("text_mala_pismena: "  + text_mala_pismena)

text_vyrez = text[6:8]
print(text_vyrez)

print("delka textu: "  + str(len(text_vyrez)))

#pismeno = text[len(text)-1]
pismeno = text[-1]
print(pismeno)
print(type(pismeno))

vstup = float(input("Zadej celke cislo: "))
print(vstup)
print(type(vstup))

print(globals())




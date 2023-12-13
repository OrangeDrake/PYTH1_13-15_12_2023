cislo = 4

if cislo < 5:
    print("cislo je mensi 5")
elif cislo > 5:
    #pass
    print("cislo je vetsi 5")
else:
    print("cislo je rovno 5")


cisla = [10,5,7,8, 15]
soucet = 0
for cislo in cisla:
    #soucet += cislo
    souce = soucet + cislo

print("Soucet cisel je: " + str(soucet))
print("Prumerna hodnota je: " + str(soucet/len(cisla)))

text = "hello word"
text_pozpatku = ""

for znak in text:
    text_pozpatku = znak + text_pozpatku

print("Puvodni text: " + text)
print("Text po zpatku: " + text_pozpatku)

for i in range(4):
    print(str(i+1) + ".: slovo")

cisla1 = [1, 2, 3, 4, 5]

vysledky = []
for i in range(len(cisla)):
    vysledky.append(cisla[i] + cisla1[i])

print("Soucet odpovidajicich cisel: " + str(vysledky))


vstup = ""
pocet_slov = 0
maximalni_pocet_pokusu = 3
while vstup != "konec":
    vstup = input("zadej slovo: ")
    pocet_slov += 1
    if pocet_slov == maximalni_pocet_pokusu:
        print("byl vycerpan maximalni pocet pokusu")
        break
print("Bylo zadano: " + str(pocet_slov))

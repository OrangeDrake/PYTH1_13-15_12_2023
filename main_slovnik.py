
vysky = {}

vysky["pepa"] = 180
vysky["zdenek"] = 175
vysky["kveta"] = 170

print("Vyska Pepi: {}". format(vysky["pepa"]))
print("Vyska Zdenka: {}". format(vysky["zdenek"]))
print("Vyska Kvety: {}". format(vysky["kveta"]))

try:
    print("Vyska Jitky: {}". format(vysky["jirka"]))
except KeyError as e:
    print(e)

if "jirka" in vysky:
    print("Vyska jirky je ulozena ")
else:
    print("Vyska jirky neni ulozena")

veta = "hello word123"

pocty_pismen = {}

for znak in veta:
    if znak.isspace() or znak.isdecimal():
        continue

    if znak not in pocty_pismen:
        pocty_pismen[znak] = 1
    else:
        pocty_pismen[znak] = pocty_pismen[znak] + 1

print(pocty_pismen)

#projiti klicu
for pismeno in pocty_pismen:
    print(pismeno)

#projiti hodnot
for pismeno in pocty_pismen:
    print(pocty_pismen[pismeno])

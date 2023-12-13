

cisla = [10, 5, 11, 12]
print(cisla)

print("cisla: " + str(cisla))

cisla.append(15)

print("cisla: " + str(cisla))

cisla.append("hello")

print("cisla: " + str(cisla))

cisla_cast = cisla[:-1]

print("cisla: " + str(cisla))
print("cisla_cast: " + str(cisla_cast))

cisla = cisla[:-1]
print("cisla: " + str(cisla))

cisla_melka_kopie = cisla
print("cisla_melka_kopie: " + str(cisla_melka_kopie))

cisla.append(100)
print("po pridani")
print("cisla: " + str(cisla))
print("cisla_melka_kopie: " + str(cisla_melka_kopie))

cisla_hluboka_kopie = cisla[:]

print("cisla: " + str(cisla))
print("cisla_hluboka_kopie: " + str(cisla_hluboka_kopie))

cisla.append(200)
print("po pridani")
print("cisla: " + str(cisla))
print("cisla_hluboka_kopie: " + str(cisla_hluboka_kopie))
import math
import numpy as np
import matplotlib.pyplot as plt
import time
import math
from scipy.interpolate import make_interp_spline
def urci_zde_je_prvocislo(cislo):
    for delitel in range(2, cislo):
        if cislo % delitel == 0:
            return False
    return True

def urci_zda_je_prvocislo_odmocnina(cislo):
    for delitel in range(2, int(math.sqrt(cislo))+1):
        if cislo % delitel == 0:
            return False
    return True


def najdi_prvocisla(urcovaci_funkce, horni_mez):
    prvocisla = []
    for cislo in range(2, horni_mez):
        if urcovaci_funkce(cislo):
            prvocisla.append(cislo)
    return prvocisla

def najdi_prvocisla_eratosthenovo_sita(horni_mez):
    prvocisla = []
    jsou_prvocisla = [True] * horni_mez
    for cislo in range(2, horni_mez):
        if jsou_prvocisla[cislo]:
            prvocisla.append(cislo)
            for nasobky in range(cislo + cislo, horni_mez, cislo):
                jsou_prvocisla[nasobky] = False
    return prvocisla


horni_mez = 100
prvocisla_podle_prvni_funkce = najdi_prvocisla(urci_zde_je_prvocislo, horni_mez)
prvocisla_podle_druhe_funkce = najdi_prvocisla(urci_zda_je_prvocislo_odmocnina, horni_mez)
prvocisla_podle_eratosthenova_sita = najdi_prvocisla_eratosthenovo_sita(horni_mez)

print("prvocisla podle prvni funkce: {}".format(prvocisla_podle_prvni_funkce))
print("prvocisla podle prvni funkce: {}".format(prvocisla_podle_druhe_funkce))
print("prvocisla podle eratosthenova sita: {}".format(prvocisla_podle_eratosthenova_sita))


# print(urci_zde_je_prvocislo(9))
# print(urci_zda_je_prvocislo_odmocnina(9))

# horni_meze = [1_000, 5_000, 10_000, 100_000]
# casy_podle_prvni_funkce = []
# casy_podle_druhe_funkce = []
# for horni_mez in horni_meze:
#     start = time.time()
#     prvocisla_podle_prvni_funkce = najdi_prvocisla(urci_zde_je_prvocislo, horni_mez)
#     konec = time.time()
#     delka_behu_prvni_funkce = (konec - start) * 1000
#     start = time.time()
#     prvocisla_podle_druhe_funkce = najdi_prvocisla(urci_zda_je_prvocislo_odmocnina, horni_mez)
#     konec = time.time()
#     delka_behu_druhe_funkce = (konec - start) * 1000
#     casy_podle_prvni_funkce.append(delka_behu_prvni_funkce)
#     casy_podle_druhe_funkce.append(delka_behu_druhe_funkce)
#
# print(casy_podle_prvni_funkce)
# print(casy_podle_druhe_funkce)
#
# x = np.array(horni_meze)
# y_prvni_funkce = np.array(casy_podle_prvni_funkce)
# y_druha_funkce = np.array(casy_podle_druhe_funkce)
#
# X_Y_Sline_prvni_funkce = make_interp_spline(x, y_prvni_funkce)
# X_Y_Sline_druha_funkce = make_interp_spline(x, y_druha_funkce)
# X_ = np.linspace(x.min(), x.max(),500)
# Y_prvni_funkce = X_Y_Sline_prvni_funkce(X_)
# Y_druha_funkce = X_Y_Sline_druha_funkce(X_)
#
#
# plt.plot(X_, Y_prvni_funkce, label = "bez odmocniny")
# plt.plot(X_, Y_druha_funkce, label = "bez odmocniny")
# plt.yscale("log")
# plt.xlabel("horni meze")
# plt.ylabel("casy")
# plt.legend()
# plt.show()
#
#
#
# print("casy podle prvni funkce: {}".format(casy_podle_prvni_funkce))
# print("casy podle druhe funkce: {}".format(casy_podle_druhe_funkce))

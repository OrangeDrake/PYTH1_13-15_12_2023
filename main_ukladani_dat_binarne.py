from osoba import *
import pickle

karel = Osoba("Karel", 20)

with open("osoba.bin", "wb") as f:
    pickle.dump(karel, f)

karel = None

print(karel)

with open("osoba.bin", "rb") as f:
    karel = pickle.load(f)

print(karel)
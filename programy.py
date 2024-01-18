# Definicja klasy
# (Szablonu, przepisu, możności)
# Camel case (każde słowo z dużej litery)
class Czlowiek:
    # Ciało klasy
    # atrybut klasy
    # Cechy wszystkich obiektów danej klasy
    gatunek = "homo sapiens"
    # Metoda inicjalizacyjna (konstruktor)
    # Wywowywana w momencie tworzenia obiektu
    def __init__(self, imie, pesel, grupa_krwii):
        print(f"Tworzę nowego Człowieka o imieniu {imie}!")
        # Atrybuty obiektu
        # Cechy obiektu
        self.imie = imie
        # adam.imie = "Adam"
        # ewa.imie = "Ewa
        # Sugestia prywatności ("_" z przodu)
        # Nie ruszaj tego, to prywatna zmienna!
        self._pesel = pesel
        # Prawdziwa prywatność
        self.__grupa_krwii = grupa_krwii
    # Metoda, czyli funkcja w klasie
    # (Pewna umiejętność)
    def przedstaw_sie(self):
        print(f"Dzień dobry, mam na imię {self.imie}")


    def przedstaw(self, drugi_czlowiek):
        print(f"Oto {drugi_czlowiek.imie}")

# Tworzenie obiektu (instancja klasy Czlowiek)
# Gotowanie dania z przepisu
# Przejście z możności do aktu
adam = Czlowiek("Adam", 100000000, "A")
ewa = Czlowiek("Ewa", 100000001, "B")
kain = Czlowiek("kain", 100000001, "B")
print(adam.gatunek)
print(ewa.gatunek)
print(adam.imie)
print(ewa.imie)

print(dir(ewa))
print(dir(Czlowiek))

adam.przedstaw_sie()
ewa.przedstaw_sie()


print(adam.imie)
adam.imie = "Przemek"
print(adam.imie)
print(kain.imie)


print(adam)
print(dir(adam))
print(str(adam))
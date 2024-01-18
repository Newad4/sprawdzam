# Napisz klasę, Programista, która będzie miała w sobie
# metodę programuj(), która wyświetli napis "Programuję..."

# Stwórz 2 instancje tej klasy i sprawdź ich działanie

# class Programista:
#     def programuj(self):
#         print("programujemy!!!")
#
# programista = Programista()
# programista.programuj()


# Zadanie 2
# Napisz klasę Pudelko, która będzie przechowywała (dowolną)
# zawartość.
#
# Podpowiedź: W środku powinien być atrybut zawartosc
# oraz metody wloz(), wyciagnij(), sprawdz_czy_jest_puste()

# class Pudelko:
#     def __init__(self, zawartosc):
#         self.zawartosc =zawartosc
#
#     def pokaz_zawartosc(self):
#         return self.zawartosc
#     print(pokaz_zawartosc())
#     # def dodaj_do_pudelka(self):
#     #     self.zawartosc = nowa_zawartosc
#
# kolo = Pudelko("nowa_zawartosc")
# pudelko = Pudelko("zawartość")
# print(pudelko.pokaz_zawartosc())
# print(pudelko.dodaj_do_pudelka())
#
# class Pudelko:
#     def __init__(self):
#         self.zawartosc = []
#
#     def wloz(self, przedmiot):
#         self.zawartosc.append(przedmiot)
#         print(f'Włożono {przedmiot} do pudełka.')
#
#     def wyciagnij(self):
#         if not self.sprawdz_czy_jest_puste():
#             przedmiot = self.zawartosc.pop()
#             print(f'Wyciągnięto {przedmiot} z pudełka.')
#             return przedmiot
#         else:
#             print('Pudełko jest puste. Nie można nic wyciągnąć.')
#
#     def sprawdz_czy_jest_puste(self):
#         return len(self.zawartosc) == 0
#
# # Przykład użycia klasy Pudelko
# pudelko = Pudelko()
#
# pudelko.wloz("Klucz")
# pudelko.wloz("Długopis")
#
# pudelko.wyciagnij()

# Zadanie 2
# Napisz klasę Narzedzie, która będzie posiadała w sobie
# metodę uzyj(), która wyświetli napis "używam narzędzia"
#
# class Narzedzia:
#     def uzyj(self):
#         print("uzywam narzędzia ")
#
# narzedzia = Narzedzia()
# narzedzia.uzyj()
#
# # Zadanie 3
# # Napisz klasę GeneratorLiczbLosowych, która
# będzie w stanie wygenerować liczby od 0 do podanego zakres

# Można też tak zrobić

class Klasa:
    pass

obiekt = Klasa()

obiekt2 = Klasa()

Klasa.atrybut = "coś"

print(obiekt.atrybut)
print(obiekt2.atrybut)
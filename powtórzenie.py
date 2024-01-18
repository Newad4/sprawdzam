# napisz program kadrowy do małej firmy

#funkcje:
#zatrudnianie
#zwalnianie
#przydzielanie pensji
#stanowiska
#lista zatrudnienia

# class UI:
#     def uruchom_menu_glowne(self):
#         print("witam w programie")
#         print("wybierz opcje ")
#         print()
#
# class kadry:
#     #zatrudnianie
#     # zwalnianie
#     def __init__(self):
#         self.lita_pracownikow = []
#     def zwroc_liste_wszystkich_pracownikow(self):
#         return self.lita_pracownikow
#     def zatrudnij(self, imie, nazwisko, stanowisko, pensja):
#         pracownik = pracownik(imie, nazwisko, stanowisko, pensja)
#         self.lita_pracownikow.append(pracownik)
#
#
#
# class pracownik:
#     # mamieć imię nazwisko stanowisko pensja
#     def __init__(self, imie, nazwisko, stanowisko, pensja):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.stanowisko = stanowisko
#         self.pensja = pensja
#     def pracuj(self):
#         print(f"{self.imie}{self.nazwisko} wlasnie pracuje")
#
# kadry= kadry()
# print(kadry.zwroc_liste_wszystkich_pracownikow())
# kadry.zatrudnij("adam", "kowaliski", "sprzdawca", 4999)
#


# napis = "ala ma kota"
# print(type(napis))
# print(dir(napis))
#
#
# print(napis.find("kota"))
#
# class Klasa:
#     pass
#
# obiekt = klasa()
#
# napis = str("Ala ma kota")
# napis.capitalize()

# Lista_ocen =[3.0,4.0,5.0]
# class student:
#     def __init__(self):
#         self.oceny = [4.0]
#     def przypisz_oceny(self,oceny):
#         self.oceny = oceny
#         pass
#
# kuba = student
# print(kuba.oceny)
# kuba.przypisz_oceny()
# print(kuba.przypisz_oceny())

# pierwsze zadanie
# class Klasa:
#     # definicja klasy
#     def __init__(self):
#         self.napis_wew = ""
#     def set_string(self):
#         self.napis_wew = input('Podaj dany napis: ')
#         # ta funkcja input zwraca napis
#         # ten napis po dodaniu do klasy słowa self to ono dpisuje do obiektu
#     def print_upper(self):
#         print(self.napis_wew.upper())
#
# obiekt = Klasa()
# obiekt.napis_wew =""
# print(type(obiekt))
# # print(dir(obiekt))
# obiekt.set_string()
# obiekt.print_upper()
# #
# class Czlowiek:
#     def __init__(self):
#         self.imie =""
#     def nadaj_imie(self):

#
# class spagetti:
#     def __init__(self, pasata, wolowina, makaron):
#         self.pasata = pasata
#         self.wolowina = wolowina
#         self.makaron = makaron
#
#     def zjedz(self):
#         print("ale dobre")
#
# moje_spagetti = spagetti(300, 300,300)
# moje_spagetti.zjedz()

class UI:
    def uruchom_menu_glowne(self):
        print("Witam w programie Kadry 3000!")
        print("Wybierz opcję:")
        print()
        temp = input("1. Wyświetl wszystkich pracowników")

class Kadry:
    # Zatrudnianie, zwalnianie, przydzielanie pensji, wyświetlanie listy
    # pracowników
    def __init__(self):
        self.lista_pracownikow = []
    def zwroc_liste_wszystkich_pracownikow(self):
        return self.lista_pracownikow

    def zatrudnij(self, imie, nazwisko, stanowisko, pensja):
        pracownik = Pracownik(imie, nazwisko, stanowisko, pensja)
        self.lista_pracownikow.append(pracownik)


class Pracownik:
    # ma mieć imię , nazwisko, stanowisko , pensję
    def __init__(self, imie, nazwisko, stanowisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.pensja = pensja
    def pracuj(self):
        print(f"{self.imie} {self.nazwisko} właśnie pracuje!")


ui = UI()
ui.uruchom_menu_glowne()



#dziodziczenie klas

class student:
    def studiuj(self):
        print("Studiuje..")

class pracownik:
    def pracuj(self):
        print("Pracuje..")
class StudujacyPracownik(student, pracownik):
    pass

ewa = student()
ewa.studiuj()

przemek = pracownik()
przemek.pracuj()

marcin = StudujacyPracownik()
marcin.studiuj()
marcin.pracuj()
#dziedziczenie klas


class zwierze:
    krolestwo ="zwierzeta"

class pies(zwierze)
    gatunek = (canes)
    rasa =

class PiesRasowy(pies)



lista= [1,2, "hej", 5, "cp tam?"]

# chce stworzyć lisę  na bazie powyższej listy
# która bedzie zawierała wyłacznie liczby
# filtrowanie
odfiltrowanie = []

for element in lista:
    if type(element)== int:
        odfiltrowanie.append(element)
print (odfiltrowanie)
# listy składane(comprehension)
odfiltrowanie = [element for element in lista if type(element)== int]
print(odfiltrowanie)
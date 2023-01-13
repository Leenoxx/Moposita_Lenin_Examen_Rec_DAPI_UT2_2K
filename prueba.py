import csv


dict_personas = [['Hola', 'hello'], ['Holaaaaa', 'hello']]
fichero = "hola.csv"
with open(fichero, encoding='utf-8') as end:
    final = open(fichero, "w", newline="")
    end = csv.writer(final, quotechar='"', quoting=csv.QUOTE_ALL)
    for linea in dict_personas:
        end.writerow(linea)

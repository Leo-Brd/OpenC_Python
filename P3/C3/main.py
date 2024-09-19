import csv

data = []

with open("P3/C3/input.csv") as fichier:
    reader = csv.DictReader(fichier, delimiter=",")
    for ligne in reader:
        print(ligne["nom"] + " a travaillé " + ligne["heures_travaillees"] + " heures !")
        data.append({"nom" : ligne["nom"], "salaire" : int(ligne["heures_travaillees"]) * 15 })

en_tete = ["nom", "salaire"]

with open("P3/C3/data.csv", "w", newline="") as fichier:
    writer = csv.DictWriter(fichier, fieldnames=en_tete)
    writer.writeheader()

    for ligne in data:
        writer.writerow(ligne)



input_str = input("Renseignez une liste de nombres : ")

liste = list(map(int, input_str.split(",")))

for elt in liste:
    print(f"{elt}, ")
print(" ")

# On calcule la somme
somme = 0
for elt in liste:
    somme += elt
print(f"somme = {somme}")
print(" ")

# On calcule la moyenne
moyenne = somme/(len(liste))
print(f"moyenne = {moyenne}")
print(" ")

# On affiche le nombre de nombres superieurs a la moyenne
nb = 0
for elt in liste:
    if (elt > moyenne):
        nb += 1
print(f"nombres superieurs a la moyenne = {nb}")
print(" ")

# On affiche le nombre de nombres pairs
nb_pairs = 0
for elt in liste:
    if ((elt % 2) == 0):
        nb_pairs += 1
print(f"nombres pairs = {nb_pairs}")
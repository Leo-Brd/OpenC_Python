
nombre_a_gauche = 10
nombre_a_droite = 50

symbole = "/"

resultat = 0

if not isinstance(nombre_a_gauche, int) or not isinstance(nombre_a_droite, int):
    print("L'un des deux nombres n'est pas un entier !")
    exit()

match symbole:

    case "+":
        resultat = nombre_a_gauche + nombre_a_droite

    case "-":
        resultat = nombre_a_gauche - nombre_a_droite

    case "*":
        resultat = nombre_a_gauche * nombre_a_droite

    case "/":
        if (nombre_a_droite == 0):
            print("Erreur: impossible de diviser par zéro.")
            exit()
        else:
            resultat = nombre_a_gauche / nombre_a_droite

    case _:
        print("Le symbole est faux !")
        exit()

print(resultat)





def salaire_mensuel(salaire_annuel):
    return (salaire_annuel / 12)

def salaire_hebdomadaire(salaire_mensuel):
    return (salaire_mensuel / 4)

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return (salaire_hebdomadaire / heures_travaillees)



salaire_annuel = float(input("Quel est votre salaire annuel ?"))

heures_travaillees = float(input("Combien d'heures travaillez vous par semaine ?"))


salaire_hebdomadaire = salaire_hebdomadaire(salaire_mensuel(salaire_annuel))

salaire_horaire = salaire_horaire(salaire_hebdomadaire, heures_travaillees)

print(f"Votre salaire horaire est de {salaire_horaire} euros.")
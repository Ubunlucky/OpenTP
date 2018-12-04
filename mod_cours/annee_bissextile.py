""" Function testant si une année, saisie par l'utilisateur, est bissextile ou non """

# Définition de la fonction
def annee_bissextile(annee):
    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")

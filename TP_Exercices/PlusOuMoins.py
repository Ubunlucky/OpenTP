""" TP : création du jeu plus ou moins """

import random
import os

# Création du nombre mystère à trouver
def nombre_mystere(niveau):
    niveau = niveau * 100
    return random.randrange(1,niveau)


def plusoumoins(nombre_joueur):
    if nombre_joueur < nombre:
        message = "C'est plus"
    elif nombre_joueur > nombre:
        message = "C'est moins"
    elif nombre_joueur == nombre:
        message = "FELICITATION !!  Vous avez découvert le nombre mystère"
    return message

print("BIENVENUE dans le jeux du Plus ou Moins".center(80))
print("Il faut trouver le nombre choisi par l'ordinateur\n".center(80))

continuer = True
tentative = 0
niveau = 4

nombre = nombre_mystere(niveau)
print(nombre)

while continuer:
    nombre_joueur = -1
    while nombre != nombre_joueur or nombre_joueur < 0 or nombre_joueur > (niveau * 100):
        # Proposition du nombre par le joueur
        print("Choisissez un nombre entre 0 et",niveau * 100,": ")
        nombre_joueur = input()
        tentative +=1
        try:
            nombre_joueur = int(nombre_joueur)
        except ValueError:
            print("Vous n'avez pas saisi un nombre valide!")
            nombre_joueur = -1
            continue
        print(plusoumoins(nombre_joueur))
        print(tentative,"tentatives")
                

    newpartie = input("\nVoulez vous refaire une partie? (O/N)\n")
    if newpartie == "n" or newpartie == "N":
        continuer = False

# Mise en pause
#os.system("pause")

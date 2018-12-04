""" TP: création d'un jeu de casino simulant le jeu de la roulette """

# Import des modules Python
import math
import random
import os

# Mes variables
partie = "O"
solde = 1000


def zcasino_roulette(numero_joueur, mise_joueur):
    # Création d'un chiffre aléatoire entre 0 et 49
    numero_roulette = random.randrange(50)
    print("La bille s'arrête sur le ",numero_roulette)

    ## Resultat Roulette et calcul des gains ##
    if numero_roulette == numero_joueur:
        resultat = "FELICITATION !!"
        gain = mise_joueur + (mise_joueur * 3)

    elif numero_roulette%2 == 0 and numero_joueur%2 == 0:
        resultat = "COULEUR NOIR !!"
        gain = math.ceil(mise_joueur / 2)
        
    elif numero_roulette%2 != 0 and numero_joueur%2 != 0:
        resultat = "COULEUR ROUGE !!"
        gain = math.ceil(mise_joueur / 2)
        
    else:
        resultat = "PERDU !!"
        gain = -mise_joueur

    # Retour des variables resultat et gain de la partie
    return resultat,gain

# Fonction mis à jour du solde joueur
def zcasino_solde(gain):
    return solde + gain


print("Début de la partie de Roulette, votre solde est de",solde,"$")
# Boucle, le jeu continue tant que le joueur le souhaite
while partie == "O":
    # Choix et Vérification du numéro du joueur
    numero_joueur = 100
    while numero_joueur < 0 or numero_joueur > 49:
        numero_joueur = input("Veuillez choisir un nombre entre 0 et 49 : ")
        numero_joueur = int(numero_joueur)


    # Choix de la mise du joueur
    mise_joueur = input("Veuillez choisir votre mise : ")
    mise_joueur = int(mise_joueur)
    
    
    # On lance la roulette et on recupére le resultat et le montant du gain
    jeu = zcasino_roulette(numero_joueur, mise_joueur)
    # On met à jour le solde du joueur
    solde = zcasino_solde(jeu[1])

    # on affiche le resultat de la partie et le nouveau sole du joueur 
    print(jeu[0],"Voici votre gain", jeu[1],"$ | Votre nouveau solde est de",solde,"$")
    
    # Continuer de jouer?
    partie = input("Voulez vous continuer à jouer? (O ou N)")

# Mise en pause
os.system("pause")


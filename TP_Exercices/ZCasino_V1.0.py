""" TP: création d'un jeu de casino simulant le jeu de la roulette """

# Import des modules Python
import math
import random
import os

# Mes variables
numero_joueur = 100

# Création d'un chiffre aléatoire entre 0 et 49
numero_roulette = random.randrange(50)
print(numero_roulette)


# Choix et Vérification du numéro du joueur
while numero_joueur < 0 or numero_joueur > 49:
    numero_joueur = input("Veuillez choisir un numéro entre 0 et 49 : ")
    numero_joueur = int(numero_joueur)

# Choix de la mise du joueur  
mise_joueur = input("Veuillez choisir votre mise : ")
mise_joueur = int(mise_joueur)


## Resultat Roulette et calcul des gains ##
# BON NUMERO : gain du joiueur = mise du joueur X 3
if numero_roulette == numero_joueur:
    gain = mise_joueur + (mise_joueur * 3)
    print("FELICITATION ! Bon numéro, vous remporté la somme de",gain,"$")

# COULEUR NOIR : gain du joiueur = mise du joueur / 2
elif numero_roulette%2 == 0 and numero_joueur%2 == 0:
    gain = mise_joueur / 2
    gain = math.ceil(gain)
    print("COULEUR NOIR ! récupérez la moitié de votre mise soit", gain,"$")

# COULEUR ROUGE: gain du joiueur = mise du joueur / 2    
elif numero_roulette%2 != 0 and numero_joueur%2 != 0:
    gain = mise_joueur / 2
    gain = math.ceil(gain)
    print("COULEUR ROUGE ! Vous récupérez la moitié de votre mise soit", gain,"$")
    
else:
    print("PERDU ! Vous perdez la somme de", mise_joueur,"$")


# Mise en pause du programme
#os.system("pause")


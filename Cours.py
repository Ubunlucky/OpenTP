import os
import mod_cours.multiplication
import mod_cours.annee_bissextile
import mod_cours.public_ip_address

# Propositions des fonctions disponibles
print("1 = Utilisation premiéres conditions")
print("2 = Fonction Table de Multiplication")
print("3 = Fonction Année Bissextile")
print("4 = Découvrir son adresse IP public")

# Input Choix de l'utilisation d'une fonction
choix = input("Entrez le numéro de la fonction à tester : ")
choix = int(choix)

if choix == 1:
    print("Pas encore disponible")
    
    # Mise en pause du programme
    os.system("pause")

elif choix == 2:
    # Input de la fonction table de multiplication
    tablede = input("Entrez un chiffre pour afficher sa table de multiplication : ")
    multiplicateur = input("Entrez un chiffre pour le nombre maximum de multiplication : ")
    tablede = int(tablede)
    multiplicateur = int(multiplicateur)

    # Utilisation de la fonction table_multiplication
    mod_cours.multiplication.table_multiplication(tablede, multiplicateur)

    
    # Mise en pause du programme
    os.system("pause")

elif choix == 3:
    # Input de la fonction année bissextile
    annee = input("Saisissez une année : ") 
    annee = int(annee)

    # Utilisation de la fonction Année Bissextile
    mod_cours.annee_bissextile.annee_bissextile(annee)
    
    # Mise en pause du programme
    os.system("pause")

if choix == 4:
    print(mod_cours.public_ip_address.public_ip())
    
    # Mise en pause du programme
    os.system("pause")
    
else:
    print("Ce choix n'existe pas !!")

    # Mise en pause du programme
    os.system("pause")

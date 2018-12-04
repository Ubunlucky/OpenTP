""" fonction Boucle affichage d'une table de multiplication en boucle """

def table_multiplication(chiffre, multiplicateur):
    """ Focntion qui affiche la table de multiplication de votre choix """
    i = 1
    while i <= multiplicateur:
        print(i,"x",chiffre,"=",chiffre * i)
        i += 1


# test de la fonction
import os
if __name__ == "__main__":
    table_multiplication(4,10)
    os.system("pause")

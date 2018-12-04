import math

def zcasino_gain(test):
    if test == "gagne":
        temp="bonjour"
        temp2="toi"
    return temp, temp2


solde = 0
def zcasino_solde(gain):
    return solde + gain

prenom = "Albet"
nom = "MURALES"
age = 58

chaine = "je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom, age)


maliste = ["fruit", "legume", "fromage"]
liste2 = ["aubergine", "cougette", "pomme"]

maliste.extend(liste2)
print("\n\n## Boucle While pour parcourir une liste")
i=0
while i<len(maliste):
    print(maliste[i])
    i+=1

print("\n\n## Boucle For pour parcourir une liste")
for item in maliste:
    print(item)

print("\n\n## Boucle fonction enumerate()")
for i, item in enumerate(maliste):
    print("à l'indice",i,"se trouve l'élément",item)

print("\n\n## Boucle fonction enumerate() liste avec indice et élément")
for item in enumerate(maliste):
    print(item)

print("\n\n## Eclater une chaine")
print(chaine.split())

print("\n\n## Merger une liste")
print(" ".join(maliste))

print("\n\n## Les compréhensions de liste")
inventaire = [("pommes",22),("melons",4),("poires",18),("fraises",76),("prunes",51),]
print(inventaire)

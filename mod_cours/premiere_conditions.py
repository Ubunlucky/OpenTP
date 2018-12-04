# Premier exemple de condition
a = 5
b = 10
if b > 0:
    if a > 0:
        print("a est positif")
    elif a < 0:
        print("a est négatif")
    else:
        print("est égal à 0")
        
    c = a-b
    if c < 0:
        print("la valeur de c est négative")
    else:
        print("la valeur de c n'est pas négative")

else:
    print("ERREUR : la valeur de b n'est pas inférieur 0")
    
print("INFORMATION : la valeur de a est:",a,"la valeur de b est:",b,"la valeur de c est:",c)





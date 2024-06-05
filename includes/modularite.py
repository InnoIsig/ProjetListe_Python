def parler(personnage, message):
    print(f"Le nom est {personnage} : il dit {message}")

def au_revoir():
    print("Au revoir !")

#pour afficher ou tester la modilarite en l'interieur du module sans avoir passe par l'appel
if __name__ == ("__main__"):
    parler("Innocent", "Bonjour")
    au_revoir()
# import math

# resultat = math.sqrt(100)

# print(resultat)

# sin = math.sin(45)
# print(sin)

# cos = math.cos(34)
# print(cos)

# tag = math.tan(57)
# print(tag)



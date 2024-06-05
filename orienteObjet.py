class Voiture:
    voiturure_crees = 0

    # creation d;une methode avec __init__ pour l'initialisation
    def __init__(self, marque):
        #Voiture.voiturure_crees +=1
        self.marque = marque

    def affiche_marque(self):
        print(f"La marque de la voiture est {self.marque}")       

# creation d'une instance
voiturure_1 = Voiture("Toyota")
voiturure_2 = Voiture("Hoah")

#affichage avec l'instance
voiturure_1.affiche_marque()
voiturure_2.affiche_marque()

#affichage directement avec la classe
Voiture.affiche_marque(voiturure_1)
Voiture.affiche_marque(voiturure_2)



#print(Voiture.voiturure_crees)
# print(voiturure_1.marque)
# print(voiturure_2.marque)

# print(voiturure_1.marque)
# print(voiturure_2.couleur)

# Voiture.marque = "Camion"
# print(voiturure_1.marque)
# print(voiturure_2.couleur)

# voiturure_1.marque = "Noah"
# voiturure_2.marque = "Juston"

# print(Voiture.marque)
# print(voiturure_1.marque)
# print(voiturure_2.marque)

class Humain:

    #attribut de la classe
    humain_crees= 0

    def __init__(self, v_prenom, v_age):
        print("Crestion d'une classe..")
        self.prenom = v_prenom
        self.age = v_age
        # self.pronom = "Innocent"
        # self.age = 28
        Humain.humain_crees += 1
        

print("Lancement du programme")

h1 = Humain("Innocent", 45)
print(f"Le prenom et age de  h1 est : {h1.prenom} qui a {h1.age} ans")
print(f"Humain existant est : {Humain.humain_crees}")

h2 = Humain("Albert", 67)
print(f"Le prenom et age de  h2 est : {h2.prenom} qui a {h2.age} ans")
print(f"Humain existant est : {Humain.humain_crees}")

#changement de l'attribut
h1.prenom = "Noella"
print(f"Le prenom et age de  h1 est : {h1.prenom} qui a {h1.age} ans")

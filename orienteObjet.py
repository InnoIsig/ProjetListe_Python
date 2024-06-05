class Voiture:
    voiturure_crees = 0
    def __init__(self, marque):
        #Voiture.voiturure_crees +=1
        self.marque = marque

    def affiche_marque(self):
        print(f"La marque de la voiture est {self.marque}")       

voiturure_1 = Voiture("Toyota")
voiturure_2 = Voiture("Hoah")
voiturure_1.affiche_marque()
voiturure_2.affiche_marque()
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
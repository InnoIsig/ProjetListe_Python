# Methode statistique : Fonction indépendante mais lié à une classe
# Methode : Fonction sur une instance(objet)
# Methode de classe : Fonction sur une classe

class Humain:

    lieu_habituelle = "TERRAIN"

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    #Creation d'une methode qui pointe sur l'instance ou objet h1
    def parler(self, message): #self = est la methode stanadard
        print(f"{self.nom} a dit {message} il a {self.age} ans seulement")

    #Methode de classe
    def change_lieu(cls, nouvelle_place):
        Humain.lieu_habituelle = nouvelle_place

    nouvelle_place = classmethod(change_lieu)

    #Methode statique
    def statistique():
        print("L'humain est classe comme tout autre etre vivant dans la chaine alimentaire")
    statistique = staticmethod(statistique)


#appel de la fonction statique
Humain.statistique()
#appel de la methode de classe
print(f"L'ancienne planette est :{Humain.lieu_habituelle} ")
Humain.nouvelle_place("Mars")
print(f"L'ancienne planette est :{Humain.lieu_habituelle} ")

#appel methode d'instance
h1 = Humain("Innocent", 23)
h1.parler("Bonjour mes camarades")

      
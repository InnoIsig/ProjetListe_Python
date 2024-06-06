class Humain:
    lieus_habitation = "Terrair"

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    #Creation d'une methode qui pointe sur l'instance ou objet h1
    def parler(self, message): #self = est la methode stanadard
        print(f"{self.nom} a dit {message} il a {self.age} ans seulement")

    def change_habitation(cls, nouvelle_place): #cls = methode de la classe
        Humain.lieus_habitation = nouvelle_place

    changer_planette = classmethod(change_habitation)

print(f"L'ancienne planette est :{Humain.lieus_habitation} ")

print(f"L'ancienne planette est :{Humain.lieus_habitation} ")
h1 = Humain("Innocent", 23)
h1.parler("Bonjour mes camarades")

      
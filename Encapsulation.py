#propriete : manière de manipuler/controler les attributs principe d'encapsulation


class Humain:
    """cette classe represente un Humain"""
    def __init__(self, nom, age):
        print("Je crée la classe Humain")
        self.nom = nom
        self._age = age

 #proprety(<getter>, <setter>, <deleter>, <helper>)
    # get permet de controler l'acces d'interdir l'acces de changer l'attribut
    def _getage(self):
        #Verification de l'age
        try:
            return self._age
        except:
            print("L'age n'existe pas")

        #Detection si l'age est 1 il faut que le programme affiche an sinon ans
        if self._age <= 1:
            return "{} {}".format(self._age, "an")
        else:
            return "{} {}".format(self._age, "ans")
    
    
    #prmet de donner l'acces aux attributs
    def _setage(self, nouvel_age):
        if nouvel_age < 0:
            self._age = 0
        else:
            self._age = nouvel_age
      
    
    

    #Permet de supprimer un attribut
    def _delage(self):
        del self._age
    
    age = property(_getage, _setage, _delage, "Je suis l'age d'un humain")
    


h1 = Humain("Innocent", 28)
print(f"{h1.nom} a {h1.age}")

#h1.age = -5
del h1.age
print(h1.age)

#affichage de l'acces help()
help(Humain)

h2 = Humain("Heritier", 45)
print(f"{h2.nom} a {h2.age}")
#h1.age = 45
#print(h1.age)
        
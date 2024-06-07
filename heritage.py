# classe mère
class Personne:
    def __init__(self, nom, postnom, matricule, age):
        self.nom = nom
        self.postnom = postnom
        self.matricule = matricule
        self.age = age

    def message(self):
        print(f"Nom: {self.nom}\nPostnom: {self.postnom}\nMatricule: {self.matricule}\nAge: {self.age}")
    
# claase fille  
class Enseignant(Personne):
    def __init__(self, nom, postnom, matricule, age, niveau):
        super().__init__(nom, postnom, matricule, age)
        self.niveau = niveau

    
    #reecrire la methode de la classe mère
    # def message(self):
    #     print("J'enseigne")

class Etudiant(Personne):
    def __init__(self, nom, postnom, matricule, age, promotion):
        super().__init__(nom, postnom, matricule, age)
        self.promotion = promotion

    # def message(self):
    #    print("Je suis le cours")
    

#petite classe
class Eleve(Etudiant):
    def __init__(self, nom, postnom, matricule, age, option, niveau):
        super().__init__(nom, postnom, matricule, age, option)
        self.option = option
        self.niveau = niveau

#programme principale
print("SITUATION ENSEIGNANT")
print("-" * 50)
E1 = Enseignant("Jean", "Albert", "001BH", 34, "Docteur")
E1.message()
print("-" * 50)

E2 = Enseignant("Jonh", "Matuidi", "001BD", 20, "Assistant")
E2.message()
print("Niveau:",E1.niveau)
print("-" * 50)

print("SITUATION ETUDIANT")
print("-" * 50)
D1 = Etudiant("Moise", "David", "23LHRG1023", 23, "LIC4")
D1.message()


print("-" * 50)
D2 = Etudiant("Anifa", "Josephine", "23LHRG1023", 23, "LIC4")
D2.message()
print("Promotion", D1.promotion)

print("SITUATION ELEVE")
print("-" * 50)
S1 = Eleve("Chritian", "Ajabu", "22lsijhe", 14, "3ème sécondaire\n", "SECRETARIAT-ADMINISTRATION\n" )
S1.message()
print("Niveau:", S1.niveau,"Option:",S1.option)

S2 = Eleve("Rehama", "Akili", "22lsijhe", 16, "4ème sécondaire\n", "SECRETARIAT-ADMINISTRATION\n" )
S2.message()
print("Niveau:", S2.niveau,"Option",S2.option)


#---------------------------------Classe multiple----------------------------
class ObjetJeu:
    pass
class Arme:
    pass
class Fusil(ObjetJeu, Arme):
    pass

#-------------------------------------Savoir si l'objet apparient à la classe-------------------------
#Fonction isinstance (<objet>, <classe>): permet de vérifier si l'objet appartient àla classe renseignée 
#issubclasse (<classe_fille>, <classe_mère>): permet de vérifier qu'une classe est fille d'une autre
class Animal:
    def __init__(self, nom):
        self.nom = nom
    def manger(self):
        print(self.nom, "je mange...")
    
class Reptille(Animal):
    def __init__(self, nom , regime_alimentaire):
        super().__init__(nom)
        self.regime_alimentaire = regime_alimentaire
    def manger(self):
        print("Le reptille mange très bien")

#programme principale
A1 = Reptille("Lezard", "grenouille")
# print(isinstance(A1, Animal))

if isinstance(A1, Animal):
    print("Lézard est un animal")
if issubclass(Reptille, Animal):
    print("Oui la classe reptile appartient à la classe Animal")




 

    
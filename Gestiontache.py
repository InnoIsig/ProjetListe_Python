import sys

def ajouter_contact(liste_contact, nom, numero):
   
    liste_contact[nom] = numero
    print(f"{nom} et a été ajouter dans vos contacts")

def supprimer_conctact(liste_contact, nom):
    if nom in liste_contact:
        del liste_contact[nom]
        print(f"{nom} a été ajouter dans vos contact")
    else:
        print(f"{nom} n'existe pas dans vos contacts")

def affiche_contact(liste_contact):
    if liste_contact:
        print("Voici les liste des contacts")
        for nom, numero in enumerate(liste_contact, 1):
            print(f"{nom}.{numero}")
    else:
        print(" La liste est vide")



def main():
  liste_contact = []

  MENU = """Choisissez parmis les options ci-dessous :
  1. Ajouter le contact 
  2. Retirer le contact
  3. Afficher le contact
  4. Quitter
     Votre choix : """
  
  MENU_CHOIX = ("1", "2", "3", "4", "5")

  while True:
    user_choix = ""
    while user_choix not in MENU_CHOIX:
          user_choix = input(MENU)
    if user_choix not in MENU_CHOIX:
        print("Choisissez seulement parmi les options demandées")


    if user_choix == "1":
        nom = input("Entrez votre nom")  
        numero = input("Enterz votre numéro")
        ajouter_contact(liste_contact, nom, numero)

    elif user_choix == "2":
        nom = input("Entrez le nom contact à supprimer")
        supprimer_conctact(liste_contact, nom)

    elif user_choix == "3":
        affiche_contact(liste_contact)

    elif user_choix == "4":
        print("A bietot")
        sys.exit()

    print("-" * 5)        
    
        
    
      



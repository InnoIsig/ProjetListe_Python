import sys


LIST = []

MENU = """" Choisissez parmis les option ci-dessous pour plannifier la tâche
1. Ajouter  une tâche
2. Rétirer une tâche
3. affiher les éléments de la tâche
4. Vider la tâche
5. Quitter la tâche
   Votre choix: """

MENU_CHOIX = ("1", "2", "3", "4", "5")

while True:
    user_choix = ""
    while user_choix not in MENU_CHOIX:
        user_choix = input(MENU)
        if user_choix not in MENU_CHOIX:
            print("Option invalide")
    
    # Pour ajouter une tâche dans la liste
    if user_choix == "1":
        item = input("Entrez l'élément à ajouter dans la tâche")
        LIST.append(item)

    # Pour retirer une tâche de la liste
    elif user_choix == "2":
        item == input("Enter l'élément à retirer dans la tâche")
        if item:
            LIST.remove(item)
        else:
            print(f"L'élément {item} n'existe pas la tâche ")

    # Pour afficher les element de tâche de la liste
    elif user_choix == "3":
        if LIST:
            print("Voici les élément de la tache")
            for i, item in enumerate(LIST, 1):
                print(f"{i}.{item}")
        else:
            print("Il y a aucun élément dans la liste")

    # Pour vider une tâche 
    elif user_choix == "4":
        if LIST:
            LIST.clear()
            print("la tâche a été vidéé avec succès")

    # Pour quitter une tâche 
    elif user_choix == "5":
        print("A bietot")
        sys.exit()

    else:
        print("-" * 80)
        


    
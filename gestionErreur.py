

# try:
#     get_utilisateur = int(input("Entrez ton age"))
# except:
#     print("Erreur de la saisie")
# else:
#     print(f"Tu as {get_utilisateur} ans")
# finally:
#     print("ET C'EST FIN DU PROGRAMME")

# nombre1 = 45

# try:
#     nombre2 = int(input("Entrez un nombre au choix"))
#     print(f"Resultat = {nombre1 / nombre2}")

# except ZeroDivisionError:
#     print("Impossible de diviser de diviser par zero")

# except ValueError:
#     print("Vous devez entrer un nombre")

# except:
#     print("Valeur incorrect")
# else:
#     print("Bravo! t'as recu")
# finally:
#     print("ET C'EST LA FIN DU PROGRAMME")

    #aasertion erreur
try:
    get_utilisateur = int(input("Entrez ton age"))
    assert get_utilisateur< 45        
except AssertionError:
    print("J'ai attrapé une erreur d'exption")




import random

def jeu_devinette():
    nombre_a_deviner = random.randint(1, 100)
    nombre_essai = 0

    print("Bienvenu dans le jeu de devinette")
    print("Je pense entre 1 et 100. Pouvez vous deviner quel est ce nombre")

    while True:
        essaie = int(input("Entrez votre divinette"))
        nombre_essai += 1

        if essaie < nombre_a_deviner:
            print(f"Le nombre  est trop petit")
        elif essaie > nombre_a_deviner:
            print(f"Le nombre  est trop grand")
        else: 
            print(f"Felicitation ! Vous avez diviner un nombre en {nombre_a_deviner} assai {'s' if nombre_a_deviner > 1 else ''}")
            break


if __name__ == "__main__":
    jeu_devinette()
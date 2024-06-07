
#classe str (Chaine de carectere)
# help(str)
"""
str.upper(): mettre en majuscule
str.lower(): mettre en minuscule
str.capitalize() : mettre la premiere de la phrase en majuscule
str.title(): mettre chaque lettre du debut de la phrase en majuscule
str.center(<largeur>, <caractere_remplissage>) 
str.find(<chaine>, <debut>, <fin>) permet de vérifier la position de chaque element dans une phrase
str.index(<chaine>, <debut>, <fin>)
str.strip(): permet d'alever les aspaces(<>)
str.raplace(<ancienne>, <nouvelle> <occurrance>)
str.isalpha(), str.isdigit(), str.isdecimal(), str.isnumeric(), str.isalphanum()
str.iskeyword(), str.isidentifier()
 Une méthode de chaine travaille sur une copie pas sur lq chaine elle-mem
"""

ma_cahine = "bonjour tout le monde"
ma_cahine = ma_cahine.capitalize()
print(ma_cahine)

mon_programme = "MonSuperProgramme"
print(mon_programme)
mon_programme = mon_programme.center(50, "-")
print(mon_programme)

ma_verication = "MonSuperPro"
try:
    print(ma_verication.index("super"))
except:
    print("Le mot n'existe pas")

ma_lettre = "acacacacaca"
print(ma_lettre)

ma_lettre = ma_lettre.replace("a", "z", 2)
print(ma_lettre)

ch = "Bonjour Monsieur"
if ch.title():
    print("C'est correcte")
    if "Bonjour" in ch:
        print("Oui c'est bien lui")
else:
    print("ce n'est pas juste")
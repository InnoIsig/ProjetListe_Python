def calcul_note(note):
    if note > 15:
        return "C'est génial"
    elif note > 13:
        return "Bon travail"
    elif note > 10:
        return "Assez bien"
    else:
        return "Attention"
    
print(calcul_note(20))

#exterieur du dossier
# import modularite


# modularite.parler("Innocent" , "Tu vas bien")
# modularite.au_revoir()

#interieur du dossier
# import includes.modularite

# includes.modularite.parler("Innocent" , "Tu vas bien")
# includes.modularite.au_revoir()

#pour simplifier
import includes.modularite as modularite

modularite.parler("Innocent" , "Tu vas bien")
modularite.au_revoir()

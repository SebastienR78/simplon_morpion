

# Fonction minimax récupère un tableau, la profondeur en entier, maximize,joueur en  en boolean
# Si on est au maximum de la profondeur
#   Appelle une fonction pour récupérer le poids de la valeur
#   Renvoie le poids
# Si maximize est vrai
#   La valeur actuelle = -1000
#   pour i de 0 à 3
#       pour j de 0 à 3 
#           modifie la valeur de ij au numéro de joueur dans le tableau
#           value = maximum entre value et minimax ( 
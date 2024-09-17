import numpy as np

# récupère un tableau 
# intialise une valeur de vérification à False
# Tant qu'elle est fausse 
#   Le joueur nnote son choix
#   Si la variable est dans la liste de possibilité
#       x = le reste du choix divisé par 3
#       y = la division du choix et de 3
#       si cette place est vide
#           initialise la condition de sortie à Vraix
    
def humanPlay(gameArray):
    emptySpace = False
    while not emptySpace:
        playerChoice = int(input("Veuillez choisir une case vide entre 1 et 9 : "))-1
        if playerChoice >=0 and playerChoice <9:
            x = playerChoice % 3
            y =  int(playerChoice / 3 )
            if gameArray[y][x] == -1 :
                emptySpace = True
    return (x,y)    

# Enregistre la valeur du joueur à sa place dans le tableau
def marq(place, array,player):
    array[place[0]][place[1]]=player
    return array
    

    
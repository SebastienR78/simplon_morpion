import numpy as np
import matplotlib.pyplot as plt

# récupère un tableau 
# intialise une valeur de vérification à False
# Tant qu'elle est fausse 
#   Le joueur nnote son choix
#   Si la variable est dans la liste de possibilité
#       x = le reste du choix divisé par 3
#       y = la division du choix et de 3
#       si cette place est vide
#           initialise la condition de sortie à Vraix
    
def humanPlay(gameArray, player):
    emptySpace = False
    while not emptySpace:
        try :
            playerChoice = int(input(f"{player}Veuillez choisir une case vide entre 1 et 9 : "))-1
            if playerChoice >=0 and playerChoice <9:
                x = playerChoice % 3
                y =  int(playerChoice / 3 )
                if gameArray[x][y] == -1 :
                    emptySpace = True
                else:
                    print("La case est déjà occupée, veuillez en choisir une autre.")
            else:
                print("Choix invalide, veuillez entrer un nombre entre 1 et 9.")
        except ValueError: 
                print('Veuillez entre un chiffre entre 1 et 9')
    return (x,y)    

# Enregistre la valeur du joueur à sa place dans le tableau
def marq(place, array,player):
    array[place[0]][place[1]]=player
    return array

# Vérifier si un joueur a gagné
def check_win(gameArray, player):
    # Vérifier les lignes et les colonnes
    for i in range(3):
        if all([gameArray[i][j] == player for j in range(3)]) or all([gameArray[j][i] == player for j in range(3)]) :
            return True
        
        # Vérifier les diagonales
    if gameArray[0][0] == player and gameArray[1][1] == player and gameArray[2][2] == player:
        return True
    if gameArray[0][2] == player and gameArray[1][1] == player and gameArray[2][0] == player:
        return True

    return False 


def draw_win_line(direction, index):
    if direction == 'row':  # Ligne horizontale
        plt.plot([0, 3], [3 - index - 0.5, 3 - index - 0.5], color='green', linewidth=5)
    elif direction == 'col':  # Colonne verticale
        plt.plot([index + 0.5, index + 0.5], [0, 3], color='green', linewidth=5)
    elif direction == 'diag':  # Diagonale principale
        plt.plot([0, 3], [3, 0], color='green', linewidth=5)
    elif direction == 'anti-diag':  # Diagonale secondaire
        plt.plot([0, 3], [0, 3], color='green', linewidth=5)
    
    plt.draw()
    plt.pause(0.001)


def computerPlay(gameArray):
    tab_empty= []
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if gameArray [i][j] == -1 :
                tab_empty.append((3*j+i))
            j+=1
        i+=1
    value =  np.random.choice(tab_empty)
    return ( value%3,int(value/3))


# La fonction iaPlay appellera la fonction minimax qui sera dans ia.py
# Il récupèrera la valeur de la fonction minimax()
# Puis la mettra en forme pour renvoyer le résultat dans le bon format

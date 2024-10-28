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
    if gameArray[0][0] == player and gameArray[1][1] == player and gameArray[2][2] == player or gameArray[0][2] == player and gameArray[1][1] == player and gameArray[2][0] == player:
        return True

    return False 
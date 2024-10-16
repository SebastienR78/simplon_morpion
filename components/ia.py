from components.service import check_win
0
# Fonction minimax récupère un tableau, la profondeur en entier, maximize,joueur en  en boolean
# Si on est au maximum de la profondeur
#   Appelle une fonction pour récupérer le poids de la valeur
#   Renvoie le poids
# Si maximize est vrai
#   La valeur actuelle = -1000
#   pour i de 0 à 3
#       pour j de 0 à 3 
#           modifie la valeur de ij au numéro de joueur dans le tableau
#           value = maximum entre value et minimax ( tableau_modifié, profondeur +1,!maximize,joueur)
#           si tableau est vide et i == 1 et j == 1
#           value +=50
# Si maximize est faux
#   La valeur actuelle = +1000
#   pour i de 0 à 3
#       pour j de 0 à 3 
#           modifie la valeur de ij au numéro de joueur dans le tableau
#           value = maximum entre value et minimax ( tableau_modifié, profondeur +1,!maximize,joueur)
#           si tableau est vide et i == 1 et j == 1
# Renvoie Value
#

def freeSpace(game)->int:
    free=0
    for i in range(0,3):
        for j in range(0,3):
            if game[i][j]==-1:
                free+=1
    return free

def  minimax(game, maximize:bool, depth:int,gamer:int):
    free=freeSpace(game)
    i_choice= -1
    j_choice = -1
    if check_win(game,gamer):
        if not maximize:
            return 5100
        return 500
    if(depth == 5 or free==1 or check_win(game,gamer)):
        if not maximize:
            return -100
        return 100
    if maximize:
        value = -1000
        for i in range(0,3):
            for j in range(0,3):
                if game[i][j]==-1:
                    game[i][j]=gamer
                    val = minimax(game, not maximize,depth+1, 1-gamer)
                    game[i][j]=-1
                    if i==1 and j==1 and depth ==0:
                        val+=50
                    if val>value:
                        value = val
                        i_choice=i
                        j_choice=j
    else:
        value = 1000
        for i in range(0,3):
            for j in range(0,3):
                if game[i][j]==-1:
                    game[i][j]=gamer
                    val =minimax(game, not maximize,depth+1, 1-gamer)
                    game[i][j]=-1
                    if i==1 and j==1 and depth==0:
                        val-=50
                    if val<value:
                        value = val
                        i_choice=i
                        j_choice=j
    if depth != 0 :
        return value
    else :
        print("i "+str(i_choice)+" j "+str(j_choice))
        return (i_choice,j_choice)
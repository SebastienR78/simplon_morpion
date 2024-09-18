from components.player import humanPlay, marq, check_win
import  components.grille as grille
import numpy as np
import matplotlib.pyplot as plt
import time

# Programme principal
#  plt.ion() met 
# initialise les valeurs de fin de boucle
# initialise un tableau avec -1 pour les cases vide
# Tant que la partie n'est pas gagnée ou qu'on n'a pas fait 9 tours
#   Le joueur 1 joue et enregistre son choix
#   le tableau enregistre sa valeur
#   la grille affiche le changement
#   Si on est à 9 lance les mêmes actions sur le joueur 2
def game():
    plt.ion()
    turn = 0
    win = False
    gameArray = np.array([[-1,-1,-1],[-1,-1,-1], [-1,-1,-1]])
    while turn <9 and not win:
        currentPlayer = turn % 2
        print(f"Tour du joueur {currentPlayer+1}")
        place = humanPlay(gameArray, currentPlayer)
        gameArray = marq(place, gameArray,currentPlayer)
        grille.afficher_grille_tot(gameArray)
        win = check_win(gameArray,currentPlayer)
        turn+=1
    if win:
        message = "Le joueur ",currentPlayer+1," a gagné"
    else:
        message = "Il y a eu égalité"
    plt.close()
    grille.afficher_grille()
    plt.text(1.5,1.5,message,fontsize=24, ha='center', va='center')
    plt.show()
    time.sleep(7)
    plt.close()

game()
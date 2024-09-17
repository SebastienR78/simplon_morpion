import components.grille as grille
import components.player as player
import numpy as np


# Programme principal
# initialise les valeurs de fin de boucle
# initialise un tableau avec -1 pour les cases vide
# Tant que la partie n'est pas gagnée ou qu'on n'a pas fait 9 tours
#   Le joueur 1 joue et enregistre son choix
#   le tableau enregistre sa valeur
#   la grille affiche le changement
#   Si on est à 9 lance les mêmes actions sur le joueur 2
def game():
    turn = 0
    win = False
    gameArray = np.array([[-1,-1,-1],[-1,-1,-1], [-1,-1,-1]])
    while turn <9 and not win:
        place = player.humanPlay(gameArray)
        gameArray = player.marq(place, gameArray,0)
        grille.afficher_grille_tot(gameArray)
        #grille.afficheX()
        if turn<9:
            player.humanPlay(gameArray)

game()
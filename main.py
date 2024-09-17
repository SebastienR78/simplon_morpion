import components.grille as grille
import components.player as player
import numpy as np

def game():
    turn = 0
    win = False
    gameArray = np.array([[-1,-1,-1],[-1,-1,-1], [-1,-1,-1]])
    while turn <9 and not win:
        place = player.humanPlay(gameArray)
        player.marq(place, gameArray,"x")
        grille.afficher_grille_tot(gameArray)
        #grille.afficheX()
        if turn<9:
            player.humanPlay()
game()
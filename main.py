from components.player import humanPlay, marq, check_win, computerPlay
import  components.grille as grille
import numpy as np
import matplotlib.pyplot as plt

# Programme principal
#  plt.ion() met 
# initialise les valeurs de fin de boucle
# initialise un tableau avec -1 pour les cases vide
# Tant que la partie n'est pas gagnée ou qu'on n'a pas fait 9 tours
#   Le joueur 1 joue et enregistre son choix
#   le tableau enregistre sa valeur
#   la grille affiche le changement
#   Si on est à 9 lance les mêmes actions sur le joueur 2
def humanGame():
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
    grille.winner(message)


# Programme principal
#  plt.ion() met 
# initialise les valeurs de fin de boucle
# initialise un tableau avec -1 pour les cases vide
# Tant que la partie n'est pas gagnée ou qu'on n'a pas fait 9 tours
#   Le joueur 1 joue et enregistre son choix
#   le tableau enregistre sa valeur
#   la grille affiche le changement
#   Si on est à 9 lance les mêmes actions sur le joueur 2
def computeGame():
    playerAnswer  =""
    plt.ion()
    turn = 0
    win = False
    gameArray = np.array([[-1,-1,-1],[-1,-1,-1], [-1,-1,-1]])
    while playerAnswer != "o" and playerAnswer != "n":
        playerAnswer= input("Voulez vous être le premier joueur ? ( O/N)").lower()
    playerTurn = playerAnswer != "o"
    while turn <9 and not win:
        currentPlayer = turn % 2
        print(f"Tour du joueur {currentPlayer+1}")
        if currentPlayer == playerTurn:
            place = humanPlay(gameArray, currentPlayer)
        else :
            place = computerPlay(gameArray)
        gameArray = marq(place, gameArray,currentPlayer)
        grille.afficher_grille_tot(gameArray)
        win = check_win(gameArray,currentPlayer)
        turn+=1
    if win:
        message = "Le joueur ",currentPlayer+1," a gagné"
    else:
        message = "Il y a eu égalité"
    grille.winner(message)


#def iaGame():


# Demande au joueur avec qu'il veut jouer
# Vérifie son entrée
# Lance le programme choisi
def choiceGame():
    choice =""
    valueWaited = ["j","o"]
    while choice not in valueWaited:
        choice = input("Voulez vous jouer avec un autre joueur (j) ? un ordi (o) ? ou une ia (va te coucher)").lower()
    if choice=="j":
        humanGame()
    elif choice == "o":
        computeGame()


choiceGame()
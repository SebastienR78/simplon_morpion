import matplotlib.pyplot as plt
import time 
# Afficher la grille et ses coordonées
# grid va afficher la grille d'arriere plan pour les courbes et pas ce qu'on recherche
# Definition des intersections à linterieur du carré
def afficher_grille() :
    plt.title("Morpion avec supplément jus de cactus")
    plt.plot([0, 3], [1, 1], 'k') 
    plt.plot([0, 3], [2, 2], 'k') 
    plt.plot([1, 1], [0, 3], 'k') 
    plt.plot([2,2], [0, 3], 'k') 
    plt.gca().axes.xaxis.set_visible(False)
    plt.gca().axes.yaxis.set_visible(False)
    plt.box(False)

# Appelle la fonction d'affiche grille
# initilise un premier increment
# parcours chaque ligne
#   initialise un deuxieme increment
#   Parcours chaques case
#   Affiche la croix ou le cercle suivant la valeur du tableau à i et j
# affiche le tableau
def afficher_grille_tot(gameArray):
    afficher_grille()
    i = 0
    while i<3:
        j = 0 
        while j<3:
            if gameArray[i][j] == 0:
                 afficher_x(i,j)
            elif gameArray[i][j] == 1:
                afficher_o(i,j)
            j+=1
        i+=1
    plt.show()

# affiche les croix
def afficher_x(x,y):
    plt.text(x+0.5,3-y-0.5,"X",fontsize=32, ha='center', va='center', color='blue')

# affiche les cercles
def afficher_o(x,y):
    plt.text(x+0.5,3-y-0.5,"O",fontsize=32, ha='center', va='center', color='red')

def winner(message):
    plt.clf()
    plt.suptitle(message,fontsize=42)
    plt.show()
    time.sleep(7)
    plt.close()
    print(message)
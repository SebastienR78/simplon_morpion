import matplotlib.pyplot as plt

# Afficher la grille et ses coordonées
# grid va afficher la grille d'arriere plan pour les courbes et pas ce qu'on recherche
 # Definition des intersections à linterieur du carré
def afficher_grille() :
    plt.plot([0, 3], [1, 1], 'k') 
    plt.plot([0, 3], [2, 2], 'k') 
    plt.plot([1, 1], [0, 3], 'k') 
    plt.plot([2,2], [0, 3], 'k') 
    plt.legend().remove()
    plt.axes("off")
    plt.show()

def afficher_grille_tot(gameArray):
    afficher_grille()
    i = 0
    j = 0 
    while i<3:
        while j<3:
            if gameArray[i][j]!= -1 and gameArray != 0:
                afficher_x(i,j)
            elif gameArray[i][j]!=-1 and gameArray != 1:
                afficher_o(i,j)
    plt.show()

def afficher_x(x,y):
    print("plot la croix")

def afficher_o(x,y):
    print("plot le o")
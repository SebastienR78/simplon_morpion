import matplotlib.pyplot as plt

# Afficher la grille et ses coordonées
# grid va afficher la grille d'arriere plan pour les courbes et pas ce qu'on recherche
 # Definition des intersections à linterieur du carré
def afficher_grille() :
    plt.plot([0, 3], [1, 1], 'k') 
    plt.plot([0, 3], [2, 2], 'k') 
    plt.plot([1, 1], [0, 3], 'k') 
    plt.plot([2,2], [0, 3], 'k') 
    plt.legend()
    plt.show()
afficher_grille()
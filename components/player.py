import numpy as np

# récupère
def humanPlay(gameArray):
    emptySpace = False
    while not emptySpace:
        playerChoice = int(input("Veuillez choisir une case vide entre 1 et 9 : "))-1
        if playerChoice >=0 and playerChoice <9:
            valuePlayer = int(playerChoice)
            x = valuePlayer % 3
            y =  int(valuePlayer / 3 )
            if gameArray[y][x] == -1 :
                emptySpace = True
    return (x,y)    

def marq(place, array,player):
    #je verifie un truc avant
    array[place[0]][place[1]]=0
    return array
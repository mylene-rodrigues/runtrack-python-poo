import math

matrice = [
  [1,0,0,1,1,0],
 [1,0,3,1,1,0],
 [1,0,0,0,3,0],
 [8,0,0,0,1,1],
 [1,0,1,0,1,0],
 [1,0,1,0,0,0],
]

def afficher_plateau(plateau):# procédure qui affiche le plateau dans la console, plateau etant une matrice contenant des entiers

        nL = len(matrice) #nbre de ligne dans la matrice
        nC = len(matrice[0]) # nbre de colonne ds la 1ere ligne

        for y in range(nL): #Pour la ligne d'index 0 à la ligne d'index max
            for x in range(nC): # Pour la colonne 0 jusqu'a la max
                caractere = carac_case(matrice[y][x])
                print(caractere, end="")
            print()

def carac_case(code): # fonction qui renvoi un caractère à afficher en fonction  du code entier fourni
    if code == 8 : 
         return chr(0x263A)
    elif code == 3 :
         return chr(0x2620)
    elif code == 1 : 
         return chr (0x25A0)
    else:
        return chr(67)

afficher_plateau(matrice)


class Personnage:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def gauche(self,x):
        self.x = x - 1
    
    def droite(self,y):
        self.y = y - 1

    def bas(self,x):
        self.x = x + 1

    def haut(self,y):
        self.y = y - 1

position = []


p1=Personnage(3,6)

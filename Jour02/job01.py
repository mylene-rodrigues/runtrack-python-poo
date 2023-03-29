class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur


a = Rectangle(10,5)
print("longueur =", a.get_longueur())
print("largeur =", a.get_largeur())
a.set_longueur(12)
a.set_largeur(10)
print("longueur =", a.get_longueur())
print("largeur =", a.get_largeur())
 

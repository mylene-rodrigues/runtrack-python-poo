class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#afficherLesPoints” qui affiche les coordonnées des points.
    def afficherLesPoints(self):
        print(self.x, self.y)
#“afficherX” et “afficherY” qui affiche respectivement “x” et “y”.
    
    def afficherX(self):
        print(self.x)

    def afficherY(self):
        print(self.y)

    def changerX(self, x2):
        self.x = x2
        print(x2)

    def changerY(self, y2):
        self.y = y2
        print(y2)

p1 = Point(2,5)
p1.afficherLesPoints() 
p1.afficherX() 
p1.afficherY()
p1.changerX(x2=6)
p1.changerY(y2=6)


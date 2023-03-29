class Forme:

	def __init__(self):
		pass

	def aire(self):
		return "O"


class Rectangle(Forme):

	def __init__(self, largeur, hauteur):
		Forme.__init__(self)
		self.largeur = largeur
		self.hauteur = hauteur

	def aire(self):
		self.aire = self.largeur * self .hauteur
		print("L'aire est de :", self.aire)


class Cercle(Forme):
	def __init__(self, rayon):
		self.rayon = rayon
		Forme.__init__(self)

	def aire(self):
		self.aire = self.rayon * self.rayon * 3.14
		print("L'aire du cercle est de :", self.aire)

forme = Forme()
print(forme.aire())

Rectangle = Rectangle(5,8)
Rectangle.aire()

Cercle = Cercle(4)
Cercle.aire()
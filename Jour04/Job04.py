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

forme = Forme()
print(forme.aire())

Rectangle = Rectangle(5,8)
Rectangle.aire()
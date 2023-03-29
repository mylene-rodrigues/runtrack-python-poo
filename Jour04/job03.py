class Rectangle:
	def __init__(self,longueur, largeur):
		self.__longeur = longueur
		self.__largeur = largeur

	def perimetre(self):
		self._perimetre = (self.__longeur + self.__largeur) * 2
		print("Le perimètre est de:", self._perimetre)

	def surface(self):
		self._surface = self.__largeur * self.__longeur
		print("La surface est de", self._surface)

	def getLongueur(self):
		return self.__longeur

	def setLongueur(self, nouvelleLong):
		self.__longeur = nouvelleLong

	def getLargeur(self):
		return self.__largeur

	def setLargeur(self, nouvelleLarg):
		self.__largeur = nouvelleLarg


class Parallelepipede(Rectangle):

	def __init__(self, longueur, largeur, hauteur):
		Rectangle.__init__(self, longueur, largeur)
		self.__hauteur = hauteur

	def volume(self):
		volume = self._surface * self.__hauteur
		print("Le volume est de ", volume)

Rectangle1 = Rectangle(5, 12)
Rectangle1.surface()
Rectangle1.perimetre()
Rectangle1.setLargeur(8)
Rectangle1.setLongueur(24)

GrandRectangle1 = Parallelepipede(7, 12, 54)
GrandRectangle1.surface()
GrandRectangle1.perimetre()
GrandRectangle1.volume()
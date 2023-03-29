import random

class Carte:

	def __init__(self):
		self._valeur = ["AS", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
		self._couleur = ["Pique", "Carreau", "Coeur", "Trefle"]
		self._paquet = [["AS", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi"],
		                ["AS", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi"],
		                ["AS", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi"],
		                ["AS", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi"]]

	def piocher(self):
		couleur = [0, 1, 2, 3]
		carte = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
		rdm1 = random.choice(couleur)
		rdm2 = random.choice(carte)
		couleurTirer = ""
		if rdm1 == 0:
			couleurTirer = "Pique"
		elif rdm1 == 1:
			couleurTirer = "Carreau"
		elif rdm1 == 2:
			couleurTirer = "Coeur"
		elif rdm1 == 3:
			couleurTirer = "Trefle"
		carteTirer = self._paquet[rdm1][rdm2]
		self._point = carte[rdm2]
		print(carteTirer, "de", couleurTirer)
		return (str(carteTirer))


#		for i in self.__valeur:
#			if i == "AS":
#				i = 1
#			else:
#				i = 11

class Jeu(Carte):

	def __init__(self):
		self.valeur = []
		self.couleur = []
		Carte.__init__(self)

	def debut(self):
		self.distribuerCarte = Carte.piocher(self) + Carte.piocher(self)


class Participant(Jeu):

	def __init__(self):
		Carte.__init__(self)
		self.main = []
		self.valeurMain = []
		resultat = 0
		i = 0
		for i in self.valeurMain:
			resultat += self.valeurMain
			if resultat > 21:
				print("Manche perdu")
		i += 1
		while resultat < 21:
			choix = input("Piocher ou Passer ?")
			if choix == "Piocher" == "piocher":
				self.main += Carte.piocher(self)
				self.valeurMain += str(self._point)
			elif choix == "Passer" == "passer":
				break
			else:
				choix = input("Je n'ai pas compris,\nPiocher ou Passer ?")


Carte1 = Carte()
Carte1.piocher()

Joueur = Participant()
Joueur.debut()


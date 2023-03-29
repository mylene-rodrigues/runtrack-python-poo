class Carte:
	def __init__(self, valeur, couleur):
		self.valeur = valeur
		self.couleur = couleur

class Jeu:
	def __init__(self):
		self.paquet = []
		for couleur in ["coeur", "pique", "carreau", "trefle"]:
			for valeur in range(2, 11):
				self.paquet.append(Carte(valeur, couleur))
				for nom_figure in ["valet", "dame", "roi"]:
					self.paquet.append(Carte(10, couleur))
					self.paquet.append(Carte(11, couleur))
	def melanger(self):
		random.shuffle(self.paquet)

	def donner_une_carte(self):
		return self.paquet.pop()

	def jouer(self):
		# M￩langer le paquet
		self.melanger()
		# Donner 2 cartes au joueur
		joueur_main = [self.donner_une_carte(), self.donner_une_carte()]
		# Donner 2 cartes au croupier
		croupier_main = [self.donner_une_carte(), self.donner_une_carte()]
		# Calculer les points des mains
		joueur_points = sum(c.valeur for c in joueur_main)
		croupier_points = sum(c.valeur for c in croupier_main)
		# Demander au joueur s'il veut prendre une carte
		while joueur_points < 21:
			choix = input("Voulez-vous prendre une carte ? (o/n)")
			if choix == "o":
				joueur_main.append(self.donner_une_carte())
				joueur_points = sum(c.valeur for c in joueur_main)
			else:
				break
				# Si le joueur n'a pas d￩pass￩ 21, le croupier joue
			if joueur_points <= 21:
				while croupier_points < 17:
					croupier_main.append(self.donner_une_carte())
					croupier_points = sum(c.valeur for c in croupier_main)
					# Afficher les mains
					print("Votre main : ", joueur_main)
					print("Main du croupier : ", croupier_main)
					# D￩terminer le vainqueur
				if croupier_points > 21 or joueur_points > croupier_points:
					print("Vous avez gagné￩ !")
				elif joueur_points == croupier_points:
					print("Egalit￩ !")
				else:
					print("Vous avez perdu !")


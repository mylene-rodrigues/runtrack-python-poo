class CompteBancaire:
	def __init__(self, numero, nom, prenom, solde, decouvert):
		self.__numero = numero
		self.__nom = nom
		self.__prenom = prenom
		self.__solde = solde
		if decouvert == 0:
			self.__decouvert = False
		else:
			self.__decouvert = True

	def afficher(self):
		if self.__decouvert == False:
			return self.__numero, self.__nom, self.__prenom, "Pas de découvert autorisé"
		else:
			return self.__numero, self.__nom, self.__prenom, "Découvert autorisé"

	def afficherSolde(self):
		return self.__solde

	def versement(self, argent):
		self.__solde += argent
		return "Nouveau Solde:", self.__solde

	def retrait(self, enlevement):
		if self.__decouvert == True:
			self.__solde -= enlevement
		else:
			if self.__solde < enlevement:
				return "Découvert non autorisé"
		return "Nouveau Solde:", self.__solde

	def agios(self):
		agios = 5
		if self.__solde < 0:
			self.__solde = self.__solde - (self.__solde * agios / 100)
			return self.__solde

	def virement(self, Recepteur, montant):
		if self.__decouvert == False:
			if self.__solde - montant >= 0:
				self.__solde -= montant
				Recepteur.versement(montant)
				return ('Virement effectué avec succès')
			else:
				return ('Fonds insuffisants pour effectuer le virement')
		else:
			self.__solde -= montant
			Recepteur.versement(montant)
			return ('Virement effectué avec succès')


Lucas = CompteBancaire(2551120, "Lucas", "Fabre", 920, 1)
print(Lucas.afficher())

print("Lucas :", Lucas.afficherSolde())

print("Lucas :", Lucas.retrait(1150))

print("Lucas :", Lucas.versement(2200))

Matthieu = CompteBancaire(251220, "Matthieu", "Geley", -250, 1)
print("Matthieu :", Matthieu.agios())

print("Lucas :", Lucas.virement(Matthieu, 300))
print("Lucas :", Lucas.afficherSolde())
print("Matthieu :", Matthieu.afficherSolde())

class Voiture:
	def __init__(self, marque, modele, annee, kilometrage):
		self.__marque = marque
		self.__modele = modele
		self.__annee = annee
		self.__kilometrage = kilometrage
		self.__en_marche = False
		self.__reservoir = 50

	#def setMarque(self):



	#def getMarque(self):



	#def setModele(self):



	#def getModele(self):



	#def setAnnee(self):



	#def getAnnee(self):



	#def setKilom(self):



	#def getKilom(self):



	def demarrer(self):
		print("le reservoir est à", self.__reservoir)
		if self.verifier_plein() > 5:
			self.__en_marche = True
			print("La voiture peut démarrer")

	def arreter(self):
		if self.__en_marche == True:
			if self.__reservoir < 5:
				self.__en_marche = False

	def verifier_plein(self):
		return self.__reservoir
Voiture1 = Voiture("Ford","Boss 601",1969, 25100)
Voiture1.demarrer()

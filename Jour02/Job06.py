class Commande:

	def __init__(self, commande, liste, status):
		self.__commande = commande
		self.__liste = liste
		if status == 1:
			etat = "en cours"
		elif status == 2:
			etat = " terminée"
		else:
			etat = "annulée"
		self.__status = etat
		self.__TVA = 5


	def ajouterPlat(self):
		self.__liste += input("ajouter un plat")
		
	
	def annulerCommande(self):
		self.__commande = "annulée"

	def calculCommand(self):
		calcul = 0
		i = 0
		for i in self.__liste:
			if i == "Pomme":
				calcul += 10
			elif i == "Banane":
				calcul += 5
			elif i == "Chocolat":
				calcul += 8
			else:
				calcul += 12
		return calcul
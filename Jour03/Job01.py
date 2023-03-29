class Ville:
	def __init__(self, nom, habitant):
		self.__nom = nom
		self.__habitant = habitant
		print("Population de la ville de", self.__nom,  ":", self.__habitant,"\n",)

	def getNom(self):
		return self.__nom

	def getHabitant(self):
		return self.__habitant

	def setHabitant(self, Hbt):
		self.__habitant = Hbt

class Personne:
	def __init__(self, nom, age, Ville):
		self.__nom = nom
		self.__age = age

	def ajouterPopulation(self, ville):
		self.Ville = ville
		Hbt = ville.getHabitant() + 1
		ville.setHabitant(Hbt)


Paris = Ville("Paris", 1000000)
Marseille = Ville("Marseille", 861635)
John = Personne("John", 45, Paris)
Myrtille = Personne("Myrtille", 4, Paris)
Chloe = Personne("Chloé", 18, Marseille)
John.ajouterPopulation(Paris)
Myrtille.ajouterPopulation(Paris)
Chloe.ajouterPopulation(Marseille)

print("Mise à jour de la ville de", Paris.getNom(), Paris.getHabitant(), "habitants.")
print("Mise à jour de la ville de", Marseille.getNom(), Marseille.getHabitant(), "habitants.")
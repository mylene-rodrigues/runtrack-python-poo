class Personne:
	def __init__(self):
		self.age = 14

	def afficherAge(self):
		print(self.age)

	def bonjour(self):
		print("Hello")

	def modifierAge(self, nombre):
		self.age = nombre


class Eleve(Personne):

	Personne().__init__()

	def allerEnCours(self):
		print("Je vais en cours")

	def affichageAge(self):
		print("J'ai", self.age, "ans")


class Professeur(Personne):

	def __init__(self, matiere):
		Personne.__init__(self)
		self.__matiereEnseignee = matiere

	def matiereEnseignee(self):
		return self.__matiereEnseignee

	def enseigner(self):
		print("Le cours va commencer")


Personne1 = Personne()
Personne1.afficherAge()

Charles = Eleve()
Charles.affichageAge()
Charles.bonjour()
Charles.allerEnCours()
Charles.modifierAge(15)
Charles.affichageAge()

Leblanc = Professeur("Histoire")
Leblanc.modifierAge(40)
Leblanc.afficherAge()
Leblanc.bonjour()
Leblanc.enseigner()
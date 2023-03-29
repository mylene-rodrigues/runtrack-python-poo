class Student:

	def __init__(self, nom, prenom, id):
		self.__nom = nom
		self.__prenom = prenom
		self.__identifiant = id
		self.__credit = 0
		self.__level = self.__studentEval()

	def add_credits(self, ajout):
		if ajout > 0:
			self.__credit += ajout
			print("Le nombre de crédits de", self.__prenom, self.__nom, "est de", self.__credit, "points")
			self.__level = self.__studentEval()
		else:
			print("La valeur ajoutée est incorrecte, crédit actuel:", self.__credit)

	def __studentEval(self):
		if self.__credit >= 90:
			return "Excellent"
		elif 90 > self.__credit >= 80:
			return "Très bien"
		elif 80 > self.__credit >= 70:
			return "Bien"
		elif 70 > self.__credit >= 60:
			return "Passable"
		elif 60 > self.__credit :
			return "Insuffisant"

	def studentInfo(self):
		print("Nom =", self.__nom,"\n"
		      "Prenom =", self.__prenom,"\n"
		      "Id =", self.__identifiant,"\n"
		      "Niveau =", self.__level, "\n")

John= Student("Doe", "John", 145)

John.add_credits(75)
John.studentInfo()

John.add_credits(5)
John.studentInfo()

John.add_credits(10)
John.studentInfo()
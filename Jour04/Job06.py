class Vehicule:

	def __init__(self, marque, modele, annee, prix):
		self.marque = marque
		self.modele = modele
		self.annee = annee
		self.prix = prix


	def informationsVehicule(self):
		print("\nLa marque du véhicule est :", self.marque,
		      "\nLe modèle du véhicule est :", self.modele,
		      "\nL'année du véhicule est :", self.annee,
		      "\nLe prix du véhicule est :", self.prix)

	def demarrer(self):
		print("Attention, je roule")

class Voiture(Vehicule):

	def __init__(self,marque, modele, annee, prix):
		self.portes = 4
		Vehicule.__init__(self, marque, modele, annee, prix)

	def informationsVehicule(self):
		Vehicule.informationsVehicule(self)
		print("Nombre de porte du véhicule :", self.portes)

	def demarrer(self):
		print("Attention, je vrombis")

class Moto(Vehicule):

	def __init__(self, marque, modele, annee, prix, roue = 2):
		self.roue = roue
		Vehicule.__init__(self, marque, modele, annee, prix)

	def informationsVehicule(self):
		Vehicule.informationsVehicule(self)
		print("Nombre de roues du véhicule :", self.roue)

	def demarrer(self):
		print("Attention, je n'ai pas de carrosserie")

Dodge = Voiture("Mustang", "Boss 302", 1969, 25000)
Dodge.informationsVehicule()
Dodge.demarrer()

Harley = Moto("Harley Davidson", "Fat Boy 114", 2023, 27000, 2)
Harley.informationsVehicule()
Harley.demarrer()
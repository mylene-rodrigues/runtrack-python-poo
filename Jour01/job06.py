class Animal:
    def __init__(self,age,prenom):
        self.age = age
        self.prenom = prenom

    def Animal(self):
        print("L'âge de l'animal:", self.age, "ans")

    def vieillir(self, age2):
        age2 = self.age + 1
        print("L'age de l'animal:",  age2,"ans" )

    def nommer(self, prenom):
        self.prenom = prenom
        print("L'animal se nomme", prenom)


p1=Animal(0,"")
p1.Animal()
p1.vieillir(0)
p1.nommer("Luna")

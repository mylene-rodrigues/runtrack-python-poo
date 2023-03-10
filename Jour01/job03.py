#méthode de classe ou statique ?
# @classmethod => permet d'apporter des changements à la méthode


class Operation:
     def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

     def addition(self):
        # return f" {self.nombre1} ({self.nombre2})"
        print(self.nombre1 + self.nombre2)



p1 = Operation(12,3)
p1.addition()


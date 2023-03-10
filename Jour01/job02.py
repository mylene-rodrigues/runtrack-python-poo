class Operation:
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def myfunc(self):
        print("Le nombre1 est" , self.nombre1)
        print("Lenombre2 est" , self.nombre2)


p1 = Operation(12,3)
p1.myfunc()
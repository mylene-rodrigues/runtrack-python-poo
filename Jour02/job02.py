class Livre:
    def __init__(self, titre, auteur,nbrep):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbrep = nbrep

    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nbrep(self):
        if self.__nbrep > 0:
            return self.__nbrep
        else:
            raise ValueError("Erreur: le nombre entier doit être un nombre entier positif")

    
    def set_nbrep(self, nbrep):
            if isinstance(nbrep, int) and nbrep > 0:
                self.__nbrep = nbrep
            else:
                print("Erreur: le nombre entier doit être un nombre entier positif")


a = Livre("Le Passeur","Lois Lowry",220)
print("titre = {}\nAuteur = {}\nNombre de page = {}\n".format(a.get_titre(), a.get_auteur(), a.get_nbrep()))
a.set_auteur("JK Rowling")
a.set_titre("Harry Potter")
a.set_nbrep(-80)

    
print("Nouveau livre = {}\nAuteur = {}\nNombre de page = {}\n".format(a.get_titre(), a.get_auteur(), a.get_nbrep()))


class Livre:
    def __init__(self, titre, auteur,nbrep):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbrep = nbrep
        self.__disponible = True
        self.verification = True
    
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
            print("Erreur: le nombre de pages doit être un nombre entier positif")
        
    def disponible(self):
        return self.__disponible
    
    def verification(self):
       if self.disponible == True:
           return True
       else:
           return False

    def emprunter(self):
        if self.emprunter():
            self.disponible == False
            print("Le livre n'est pas disponible")
        else:
            print("Le livre est disponible")


    def rendre(self):
        if not self.disponible():
            self.__disponible = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Le livre n'a pas été emprunté, impossible de le rendre.")

livre = Livre("Le Passeur","Lois Lowry", True)
dispo_livre  = livre.verification

print(dispo_livre)


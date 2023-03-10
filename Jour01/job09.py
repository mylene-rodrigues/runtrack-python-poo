class Produit:
    def __init__(self, nom,prixHT,TVA = 0.2):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    def CalculerPrixTTC(self):
        return self.prixHT * (1 +self.TVA)
    def afficher(self):
        return "Nom du produit : {}/n PrixHT: {}€/n Prix TTC: {}€".format(self.nom,self.prixHT,self.TVA,self.CalculerPrixTTC())

 def changeNomProduit(self):

 def InfoProduit(self):
    
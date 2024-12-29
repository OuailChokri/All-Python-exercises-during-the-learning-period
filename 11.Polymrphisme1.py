class employe :
    def __init__(self,salaire):
        self.salaire = salaire
    #Exemple de Surcharge de méthode en python :
    def Calculsalaire(self,commission=None):
        if commission is None :
             print(self.salaire)
        else :
             print(self.salaire+commission)
s1= employe(1000)
s1.Calculsalaire(500)

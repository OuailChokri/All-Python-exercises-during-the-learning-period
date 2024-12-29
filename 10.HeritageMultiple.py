import datetime
#Class 1 :
class Personne :
    def __init__(self,nom,prenom,datenaissance):
        self.nom = nom
        self.prenom = prenom
        self.datenaissance = datenaissance
    def AfficherInfos(self):
        print("Nom : ",self.nom ,"\nPrenom : ",self.prenom,"\n( Date de Naissance : "
           ,self.datenaissance,")")
#Class 2 :        
class Employe :
    def __init__(self,code,salaire):
        self.code = code
        self.salaire = salaire
    def AfficherInfos(self):
        print("Code : ",self.code , "\nSaliare : ",self.salaire,"DH")
#Class 3 :(Class 3 qui Herit dans les deux class(class 1 et 2)):        
class Prof(Personne,Employe):
    def __init__(self,nom,prenom,datenaissance,code,salaire,specialite):
        Personne.__init__(self,nom,prenom,datenaissance)
        Employe.__init__(self,code,salaire)
        self.__specialite = specialite
    def AfficherInfos(self):
        Personne.AfficherInfos(self)
        Employe.AfficherInfos(self)
        print("Specialite : ",self.__specialite)
E1 = Prof("Alaoui","Safiya",datetime.date(1999,5,15),1000,1500,"Back-End")
E1.AfficherInfos()

        

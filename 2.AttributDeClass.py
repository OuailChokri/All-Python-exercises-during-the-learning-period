class Auteur :
    def __init__(self,nom,prenom):
        self.__nom = nom
        self.__prenom = prenom
    def getNom(self) :
        return self.__nom
    def setNom(self,n) :
        self.__nom = n
    def getPrenom(self) :
        return self.__prenom
    def setPrenom(self,p) :
        self.__prenom = prenom
    def Affichage(self):
        print("nom: ",self.__nom,"Prenom: ",self.__prenom)
    
class EditFour :
    def __init__(self,nom,ville,pays):
        self.__nom = nom
        self.__ville = ville
        self.__pays = pays
    def getNom(self) :
        return self.__nom
    def setNom(self,n) :
        self.__nom = n    
    def getVille(self):
        return self.__ville
    def setVille(self,v):
        self.__ville = v
    def getPays(self):
        return self.__pays
    def setPays  (self,p):
        self.__pays = p
    def Affichage(self):
        print("nom: ",self.__nom,"ville: ",self.__ville,"pays : ",self.__pays)
        
class Livre :
    cmp = 0
    def __init__(self,titre=None,auteur=None,anneePub=None,editeur=None,NbrePages=None,fournisseur=None,prix=None):
        self.__titre = titre
        self.__auteur = auteur
        self.__anneePub = anneePub
        self.__editeur = editeur
        self.__NbrePages = NbrePages
        self.__fournisseur = fournisseur
        self.__prix = prix
        Livre.cmp+=1
    def getTitre(self):
        return self.__titre
    def setTitre(self,titre):
        self.__titre = titre
    def getAuteur(self):
        return self.__auteur
    def setAuteur(self,auteur):
        self.__auteur = auteur      
    def getAnneePub(self):
        return self.__anneePub
    def setAnneePub(self,anneePub):
        self.__anneePub = anneePub    
    def getEditeur(self):
        return self.__editeur
    def setEditeur(self,editeur):
        self.__editeur = editeur

    def getNbrePages(self):
        return self.__NbrePages
    def setNbrePages(self,NbrePages):
        self.__NbrePages = NbrePages
        
    def getFournisseur(self):
        return self.__fournisseur
    def setFournisseur(self,fournisseur):
        self.__fournisseur = fournisseur
    def getPrix(self):
        return self.__prix
    def setPrix(self,prix):
        self.__prix = prix

    def Affichage(self):
        print("Les infos du livre :",self.__titre," ",self.__NbrePages,
              " ",self.__anneePub," ",self.__prix,"Infos auteur :")
        self.__auteur.Affichage()
        print("Infos fourniseur :")
        self.__fournisseur.Affichage()
        print("Infos Editeur")
        self.__editeur.Affichage()
   # def Comparer(self,l2):
      #  if self.__titre==12.__titre:
      #      print("Livre identiques")
      #  else :
      #      print("Livre différent!!")
l1 = Livre()
l1.setTitre("Livre1")
l1.setNbrePages(20)
l1.setPrix(200)
l1.setAnneePub(2021)
l1.setAuteur(Auteur("aut2","preAut1"))
l1.setFournisseur(EditFour("nomFour1","Paris","France"))
l1.setEditeur(EditFour("nomFour1","Paris","France"))
l1.Affichage()
print("Nombre de Livres : ",Livre.cmp)
#l1.Comparer(12)

l2 = Livre()
l2.setTitre("Livre2")
l2.setNbrePages(20)
l2.setPrix(200)
l2.setAnneePub(2021)
l2.setAuteur(Auteur("aut2","preAut2"))
l2.setFournisseur(EditFour("nomFour2","Paris","France"))
l2.setEditeur(EditFour("nomFour2","Paris","France"))
l2.Affichage()
print("Nombre de Livres : ",Livre.cmp)





        
















































        





























        
        
        

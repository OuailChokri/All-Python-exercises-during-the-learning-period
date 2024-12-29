from datetime import date
class livre :
    def __init__(self,isbn=None,titre=None,noms=None,datepub=None,prix=None
                 ,nomedition=None):
        self.__ISBN = isbn
        self.__Titre = titre
        self.__NomsAuteurs = noms
        self.__DatePub = datepub
        self.__Prix = prix
        self.__NomEdition = nomedition
    def __str__(self):
        return "ISBN : "+str(self.__ISBN) +"\nPrix :  "+str(self.__Prix)+"\nTitre : "+str(self.__Titre)+"\nAuteur : "+str(self.__NomsAuteurs)+"\nDate De Publication : "+str(self.__DatePub)+"\nNomEdition : "+str(self.__NomEdition)
    def Promotion (self,taux):
        self.__Prix -= (self.__Prix*taux)/100
    def getNomsAuteurs(self):
        return self.__NomsAuteurs
L=[]    
L = [livre(11,"L11",["x","y"],date(1965,10,16),500,"Ed1"),
     livre(11,"L22",["xt","y"],date(1965,10,16),500,"Ed1"),
     livre(33,"L33",["xh","y"],date(1965,10,16),500,"Ed1")]


for l in L :
  print(l)
  nom = input("Donner nom l'auteur :")
listeLivres = []
for l in L :
    if nom in l.getNomsAuteurs() :
        existe = False
        for res in listeLivres :
            if res.ComparerLivres(l)==True :
                existe = True
            if existe == False :
                listeLivres.append(l)
print("La liste des livres de cet auteur :")
for l in listeLivres :
    print(l)

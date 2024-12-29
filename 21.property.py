from datetime import date
class livre :
    def __init__(self,isbn=None,titre=None,noms=None,datepub=None,prix=None,NomEdition=None):
        self.__ISBN = isbn
        self.__Titre = titre
        self.__NomsAuteurs = noms
        self.__DatePub = datepub
        self.__Prix = prix
        self.__NomEdition = NomEdition
    def __str__(self):
        return "ISBN :"+str(self.__ISBN) + "\nprix : "+str(self.__prix)
    def getISBN(self):
        return self.__ISBN
    def setISBN(self,isbn):
        self.__ISBN = isbn
    def getPrix(self):
        return self.__Prix
    def setPrix(self,prix):
        self.__Prix = prix

L = livre()
ISBN = property(getISBN,setISBN)
Prix = property(getPrix,setPrix)

L.ISBN="hhhh"
L.Prix="ggg"
print(L)
    

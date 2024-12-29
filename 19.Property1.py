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
        return "ISBN :"+str(self.__ISBN)
    @property
    def ISBN(self):
        return self.__ISBN
    @ISBN.setter
    def ISBN(self,i):
        self.__ISBN = i
l1 = livre(205,"L11","h",date(2001,2,3),500,18)
print("Isbn :",l1.ISBN)
l1.ISBN="HHH"
print(l1)
        

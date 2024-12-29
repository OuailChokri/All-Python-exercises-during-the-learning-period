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
    @property
    def ISBN(self):
        return self.__ISBN
    @ISBN.setter
    def ISBN(self,i):
        self.__ISBN = i
    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self,e):
        self.__prix = e
l1 = livre()
l1.ISBN = int(input("Donner l'isbn : "))
l1.prix=input("Donner le prix : ")
print(l1)




    




















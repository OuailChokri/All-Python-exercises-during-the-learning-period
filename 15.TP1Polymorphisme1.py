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
      
L = livre (10,"Lord Of The Rings","JRR.Tolkien",date(1965,5,15),2000,"ED1")          
print(L)        
        

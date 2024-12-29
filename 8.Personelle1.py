class stagiaire:
    #constructeur:
    def __init__(self,numinscription,age,nom,prenom,note1,note2):
        self.__numinscription = numinscription
        self.__age = age
        self.__nom = nom
        self.__prenom = prenom
        self.__note1 = note1
        self.__note2 = note2
    def calculMoy(self):
        moy=(self.__note1+self.__note2)/2
        return moy

    def getnuminscription(self):
        return self.__numinscription 
    
    def setnuminscription(self,numinscription):
       self.__numinscription = numinscription

    def getage(self):
        return self.__age  
    def setage(self,age):
        self.__age=age
    def getnom(self):
        return self.__nom
    def setnom(self,nom):
        self.__nom=nom
    def getprenom(self):
        return self.__prenom 
    def setprenom(self,prenom):
        self.__prenom=prenom
    
    def getnote1(self):
        return self.__note1
    def setnote1(self,note1):
        self.__note1=note1
    
    def getnote2(self):
        return self.__note2
    def setnote2(self,note2):
        self.__note2=note2
    def affichage(self):
        print("Numero d'inscription : ",self.__numinscription,"\nAge : ",self.__age,"\nNom : ",self.__nom,"\nPrenom : ",self.__prenom,"\nNote1 : ",self.__note1,
              "\nNote2 : ",self.__note2,"\nMoyenne : ",self.calculMoy())
#objet d stagiaire n1 >>>>>s1:
print("STAGIAIRE : ")
s1=stagiaire(1122,21,"khalo","oulid",12.2,16)
s1.affichage()
s1.calculMoy()
#objet d stagiaire n2 >>>>>s2:
print("STAGIAIRE : ")
s2=stagiaire(77,18,"chakir","wail",15.2,18)
s2.setnuminscription(5)
s2.setage(20)
s2.setnom("chokri")
s2.setprenom("Ouail")
s2.setnote1(10)
s2.setnote2(10)
s2.affichage()
s2.calculMoy()
#Afficher les stagiaire avec la moyenne la plus elevée:
if s1.calculMoy()>s2.calculMoy():
    print("Cet stagiaire Plus eleveé : ",s1.getnom())
elif s1.calculMoy<s2.calculMoy():
    print("Cet stagiaire Plus eleveé : ",s2.getnom())










    
    

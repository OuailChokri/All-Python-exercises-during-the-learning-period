#_________________________________________________________________
class stagiaire:
    #constructeur:
    def __init__(self,num,age,nom,prenom,note1,note2):
        self.numinscription = num
        self.age = age
        self.nom = nom
        self.prenom = prenom
        self.__note1 = note1
        self.__note2 = note2
    def affichage(self):
        print("Mon numéro:",self.numinscription)
        print("Mon age",self.age)
        print("Mon nom et prenom:",self.nom,"",self.prenom)
        print("Les notes",self.__note1,"",self.__note2)
    def calculMoy(self):
        moy=(self.__note1+self.__note2)/2
        print("la moyenne:",moy)
    def getnote1(self):
        return self.__note1
    def setnote1(self,note1):
        self.__note1=note1
    def getnote2(self):
        return self.__note2
    def setnote2(self,note2):
        self.__note2=note2
        
#création des objet:
s1=stagiaire(1000,20,"chokri","wail",12,13) 
s1.affichage()
s1.calculMoy()
s2=stagiaire(2000,40,"pali","mohamed",10,5) 
s2.affichage()
s2.calculMoy()

s1.setnote1(15)
s1.setnote2(20)
s1.calculMoy()


Moy1=(s1.getnote1()+s1.getnote2())/2
Moy2=(s2.getnote1()+s2.getnote2())/2
print("--Majorant--")
if Moy1>Moy2:
    s1.affichage()
elif Moy1<Moy2:
    s2.affichage()
else:
    print("Moyennes identique!Bravo")
    






#_________________________________________________________________

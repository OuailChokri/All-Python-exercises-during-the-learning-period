from abc import abstractmethod
class Comparable :
    @abstractmethod
    def CompareTo(self):
        pass
#Les classes implémentent l'interface :
class Personne(Comparable):
    def __init__(self,nom,age):
        self.__nom = nom
        self.__age = age
    def CompareTo(self,p):
        if self.__age==p.__age:
            return True
        else :
            return False
class Outils (Comparable):
    def __init__(self,long,prix):
        self.__longueur = long
        self.__prix = prix
    def CompareTo(self,o):
        if self.__longueur ==o.__longueur:
            return True
        else :
            return False
#OBJECTS /:
p1 = Personne("n1",19)
p2 = Personne("n2",20)
o1 = Outils(60,450)
o2 = Outils(60,450)
if (p1.CompareTo(p2)):
    print("ont le meme age")
else :
    print("ages différent")
if (o1.CompareTo(o2)):
    print("Meme Longueur")
else :
    print("Longueur Different")

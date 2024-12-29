from abc import ABC , abstractmethod
#class Abstrait :

class Vehicule(ABC):
    def __init__(self,code,prix,marque,couleur,capacite):
        self._code = code
        self._prix = prix
        self._marque = marque
        self._couleur = couleur
        self._capacite = capacite
    def AfficherInfos(self):
        print("code : "+str(self._code),"prix : "+str(self._prix))
    @abstractmethod
    def setcode (self,code):
        pass
class Moto(Vehicule):
    def __init__(self,code,prix,marque,couleur,capacite,v):
        super().__init__(code,prix,marque,couleur,capacite)
        self._vitesse = v
    def AfficherInfos(self):
        super().AfficherInfos()
        print("I'm Moto with Vitesse : ",self._vitesse)
    def setcode(self,x):
        self._code = x
v = Moto(20,15000,"M1","Gris",250,20)
v.AfficherInfos()
#ve = Vehicule(20,15000,"M1","Gris",250,20)
#ve.AfficherInfos()

#Can't instantiate abstract class Because is class abstrait !
    

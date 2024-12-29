from abc import ABC,abstractmethod
#Class abstrait :

class Vehicule(ABC):
    @abstractmethod
    def PrintInfos(self):
        pass
    def Aug_Vitesse(self,x):
        self.vitesse += x
class Moto (Vehicule):
    def __init__(self,v):
        self.vitesse = v
    def PrintInfos(self):
        print("I'm Moto with Vitesse :" , self.vitesse)
v = Moto(20)
v.PrintInfos()
v.Aug_Vitesse(10)
v.PrintInfos()

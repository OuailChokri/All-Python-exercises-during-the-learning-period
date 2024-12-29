import math
from abc import ABC , abstractmethod
class Forme(ABC):
    def __init__(self,couleur):
        self.couleur = couleur
    @abstractmethod
    def surface(self):
        pass
    @abstractmethod
    def perimetre(self):
        pass
class Cercle(Forme):
    def __init__(self,rayon,couleur):
        super().__init__(couleur)
        self.rayon = rayon
    def surface(self):
        return math.pi*self.rayon
    def perimetre(self):
        return 2*math.pi*self.rayon
class Rectangle(Forme):
    def __init__(self,lar,lon,couleur):
        super().__init__(couleur)
        self.lar = lar
        self.lon = lon
    def surface(self):
        return self.lar*self.lon
    def perimetre(self):
        return 2*(self.lar+self.lon)
f= Cercle(5,'blue')
print(f.surface())
print(f.perimetre())
f= Rectangle(2,5,"juane")
print(f.surface())
print(f.perimetre())

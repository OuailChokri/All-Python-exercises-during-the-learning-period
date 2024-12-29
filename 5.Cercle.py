from math import pi
class Cercle :
    def __init__(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r
    def perimetre(self):
        return 2*pi*self.r
    def surface(self):
        return pi*self.r**2
    def testAppartenance(self,x,y):
        return (x-self.a)**2+(y-self.b)**2 == self.r**2

monCercle = Cercle(0,0,1)
print("Le périmetre du cercle est : ",monCercle.perimetre())
print("Le surface du cercle est : ",monCercle.surface())
print("Test appartenance du point est (0,1): ",monCercle.testAppartenance(0,1))


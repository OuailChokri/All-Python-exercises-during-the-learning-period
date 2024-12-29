import math 
class   Point :
    def __init__(self,x=None,y=None):
        self.__x = x
        self.__y = y
    #Get et set :
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self,x):
        self.__x = x
    def setY(self,y):
        self.__y = y
    def Afficher(self):
        return f"(x : {self.__x} , y : {self.__y})"
class GeoVecteur :
    def __init__(self,extA=None,extB=None):
        self.__extrimA = extA
        self.__extrimB = extB
    def getExtA(self):
        return self.__extrimA
    def setExtA(self,extA):
        self.__extrimA = extA
    def getExtB(self):
        return self.__extrimB
    def setExtB(self,extB):
        self.__extrimB = extB
    def Longeuer(self):
        val1 = (self.__extrimA.getX()-self.__extrimB.getX())**2
        val2 = (self.__extrimA.getY()-self.__extrimB.getY())**2
        return math.sqrt(val1+val2)
    def Afficher (self):
       # print("ExtremitéA: (",self.__extrimA.getX(),",",self.__extrimA.getY(),")")
       # print("ExtremitéB: (",self.__extrimB.getX(),",",self.__extrimB.getY(),")")
       print("ExtremitéA : ",self.__extrimA.Afficher())
       print("ExtremitéB : ",self.__extrimB.Afficher())
       print("Longeuer : ",v1.Longeuer())
v1 = GeoVecteur()
p1 = Point(12,8)
v1.setExtA(p1)
p2 = Point(15,6)
v1.setExtB(p2)
v1.Afficher()

p3 = Point(16,17)
p4 = Point(5,0)
v2 = GeoVecteur(p3,p4)
v1.Afficher()

        
    












        
        
    
    

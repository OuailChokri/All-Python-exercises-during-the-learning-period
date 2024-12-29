from math import sqrt
class Point :
    def __init__(self,a=0,b=0):
        self.x = a
        self.y = b
    def Distance(self,P):
        return sqrt((self.x-P.x)**2+(self.y-P.y)**2)
    def Milieu(self,P):
        return Point((self.x+P.x)/2,(self.y+P.y)/2)
P1=Point()
P2=Point(-1,3)
print(P1.Distance(P2))
M=P1.Milieu(P2)
print(M.x,M.y)

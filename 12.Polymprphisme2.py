class employe :
    def __init__(self,salaire):
        self.salaire = salaire
    def calculsalaire(self,comission = None):
        if comission is None :
            print(self.salaire)
        else :
            print(self.salaire+comission)
    def __add__(self,e):
        return self.salaire + e.salaire 
    def __lt__(self,e):
        if self.salaire < e.salaire :
           return True
        else :
            return False
s1 = employe(3000)
s1.calculsalaire(2000)
s2 = employe (1500)
print(s1+s2)
if s1 < s2 :
    print("S1 \: le plus petit salaire !")
else :
    print("S2 \: le plus petit salaire !")
    


class Voiture:
    def __init__(self, kilometre, nbr_accident):
        self.__kilometre = kilometre
        self.__nbr_accident = nbr_accident
    
    def get_kilometre(self):
        return self.__kilometre
    
    def set_kilometre(self, value):
        self.__kilometre = value
    
    def get_nbr_accident(self):
        return self.__nbr_accident
    
    def set_nbr_accident(self, value):
        self.__nbr_accident = value
voiture1 = Voiture(10000, 2)
print(voiture1.get_kilometre())   
voiture1.set_kilometre(12000)
print(voiture1.get_kilometre())   

print(voiture1.get_nbr_accident())   
voiture1.set_nbr_accident(3)
print(voiture1.get_nbr_accident())   

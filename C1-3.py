class Mammifere:
    def __init__(self, genre, type, famille):
        self.genre = genre
        self.type = type
        self.famille = famille
class Herbivore(Mammifere):
    def __init__(self, genre, type, famille, nom, taille):
        super().__init__(genre, type, famille)
        self.nom = nom
        self.taille = taille

class Carnivore(Mammifere):
    def __init__(self, genre, type, famille, nom, taille):
        super().__init__(genre, type, famille)
        self.nom = nom
        self.taille = taille
cheval = Herbivore("Equus", "Mammifère", "Equidés", "Cheval", 1.5)
lion = Carnivore("Panthera", "Mammifère", "Félidés", "Lion", 2.5)

print(cheval.genre)   
print(lion.famille)   
print(cheval.nom)     
print(lion.taille)    

#HERITAGGGGGGGGGE

#EX//2:
class Rectangle:
    nb_rectangles = 0  
    
    def __init__(self, longueur=1, largeur=1):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = "rectangle"
        Rectangle.nb_rectangles += 1
    
    def perimetre(self):
        return 2 * (self.longueur + self.largeur)
    
    def surface(self):
        return self.longueur * self.largeur
    
    def afficher(self):
        print(f"{self.nom} de dimensions {self.longueur} x {self.largeur} :")
        print(f" - périmètre : {self.perimetre()}")
        print(f" - surface : {self.surface()}")
class Carre(Rectangle):
    def __init__(self, A=1):
        super().__init__(longueur=A, largeur=A)
        self.nom = "carré"
        print(f"Nombre d'objets Rectangle_carré créés : {Rectangle.nb_rectangles}")
R1 = Rectangle(10,5)
R1.afficher()
C = Carre(6)
C.afficher()

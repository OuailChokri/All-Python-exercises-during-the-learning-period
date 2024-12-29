#EX3//:
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    
    def afficher(self):
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Âge: {self.age}")

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, cin):
        super().__init__(nom, prenom, age)
        self.cin = cin
        
        
class Employer(Personne):
    def __init__(self, nom, prenom, age, statue, fonction):
        super().__init__(nom, prenom, age)
        self.__statue = statue
        self.fonction = fonction
        self.__salaire = None
        
    def montant_S(self, nbh, prix_h):
        self.__salaire = nbh * prix_h
        return self.__salaire
   
    def afficher(self):
        super().afficher()
        print(f"Statue: {self.__statue}, Fonction: {self.fonction}, Salaire: {self.__salaire}")
        

    def get_salaire(self):
        return self.__salaire
    
    def set_salaire(self, new_salaire):
        self.__salaire = new_salaire
        
        
class Chef(Employer):
    def __init__(self, nom, prenom, age, statue, fonction, departement):
        super().__init__(nom, prenom, age, statue, fonction)
        self.departement = departement
        
    def montant_S(self, nbh, prix_h):
        self.__salaire = nbh * prix_h + 2000
        return self.__salaire

E1 = Employer("ouail","chokri",19,"Good","developper")
E1.afficher()
#Heritagggggggggggggggggggggggge

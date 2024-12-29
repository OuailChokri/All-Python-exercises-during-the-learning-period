class Personne :
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
    def Affichage (self):
        print("Nom : ",self.nom,"\nPrenom : ",self.prenom)
class Stagiaire(Personne) :
    def __init__(self,nom,prenom,notes):
        super().__init__(nom,prenom)
        self.notes = notes
    def AffichageNotes (self):
        print("Les Notes : ",self.notes)
    def MoyenneNotes(self):
        return sum(self.notes)/len(self.notes)
    def AffichageMoyenne(self):
        print("La moyenne est : ",self.MoyenneNotes())
    def AfficherInfo(self):
        super().Affichage()
        self.AffichageNotes()
        self.AffichageMoyenne()
         
#Ouail :
print("STAGIAIRE N°:1----")
S1 = Stagiaire ("Ouail","Chokri",[10,15,20])
S1.AfficherInfo()
print("\nSTAGIAIRE N°:2----")
#Khalid :
S2 = Stagiaire ("Khalid","melo",[6,5,10])
S2.AfficherInfo()


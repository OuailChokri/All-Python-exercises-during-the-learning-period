class CompteBancaire :
    def __init__(self,numeroCompte,nom,solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde
    def versement(self,s):
        self.solde = self.solde + s
    def retrait(self,s):
        self.solde = self.solde - s
    def __str__(self):
        return "Compte numéro :" +str(self.numeroCompte)+"\nNom et prenom :" +self.nom+"\nSolde :" +str(self.solde)

MonCompte = CompteBancaire(20220417,"Ouail Chokri",20000)
MonCompte.versement(5000)
MonCompte.retrait(1500)


print(MonCompte)




class Eleve :
    def __init__(self,nom,notes,):
        self.nom = nom
        self.notes = notes
    def Moyenne(self):
        return sum(self.notes)/len(self.notes)
    def __str__(self):
        return "Nom & Prenom :" +self.nom +"\nMoyenne :" +str(self.Moyenne())

Ouail = Eleve("Ouail Chokri",[14,15,16])
print(Ouail)

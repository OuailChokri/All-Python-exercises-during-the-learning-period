class Personne :
    def __init__(self,cin=None,nom=None,prenom=None):
        self._cin = cin
        self._nom = nom
        self._prenom = prenom
    @property
    def cin(self):
        return self._cin
    @cin.setter
    def cin(self,cin):
        self._cin = cin
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self,nom):
        self._nom = nom
    @property
    def prenom(self):
        return self._prenom
    @prenom.setter
    def prenom(self,prenom):
        self._prenom = prenom
    def __str__(self):
        return f"Cin : {self.cin} \nNom : {self.nom}\nPrenom : {self.prenom}"
class Vacciné(Personne):
    def __init__(self,cin,nom,prenom,codev,datev):
        super().__init__(cin,nom,prenom)
        self.__codev = codev
        self.__datev = datev
    def getcodev(self):
        return self.__codev
    def setcodev(self,v):
        self.__codev = v
    def getdatev(self):
        return self.__datev
    def setdatev(self,d):
        self.__datev = d
    def __str__(self):
        return super().__str__()+f"Code Vacciné : {self.__codev}\nDate Vacciné : {self.__datev}"
class vaccin :
    def __str__(self,codev,nomv,dureev):
        self.__codev = codev
        self.__nomv = nomv
        self.__dureev = dureev
    @property
    def codev(self):
        return self.__codev
    @codev.setter
    def codev(self,v):
        self.__codev = v
    @property
    def nomv(self):
        return self.__nomv
    @nomv.setter
    def nomv(self,v):
        self.__codev = v
    @property
    def dureev(self):
        return self.__dureev
    @dureev.setter
    def dureev(self,v):
        self.__dureev = v
    def __str__(self):
        return f"Code Vaccin : {self.__codev}\nNom vaccin : {self.__nomv}\nDurre entre Dose : {self.__dureev}"
class Dose :
    def __init__(self,coded,vacciné,vaccin,datep,datepd,dateEFD):
        self.__coded = coded
        self.__vacciné = vacciné
        self.__vaccin = vaccin
        self.__datep = datep
        self.__datepd = datepd
        self.__dateEFD = dateEFD
    def __str__(self):
        return "coded : "+self.__coded+" vacciné : "+self.Vacciné.__str__()+" vaccin :"+self.vaccin.__str__()+"datep : "+self.__datep+" datepD : "+self.__datpd+" dateEFD : "+self.dateEFD
#
class CentreVaccination :
    def __init__(self,nomC=None,adrr=None,listeVaccin=None,listeVacciné=None,listeDose=None):
        self.__nomC = nomC
        self.__adresse = adrr
        self.__listeVacciné = listeVacciné
        self.__listeDose = listeDose
    def rechercherVaccin(self,codeVaccin):
        for v i in list.__listeVaccin :
            if v.codev
        


















        

        

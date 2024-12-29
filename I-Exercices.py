#Ex1 :

nom=input("entrez votre nom :")
age=int(input("entrez votre age :"))
print("bounjour "+nom,"tu as",+age)

#Ex2 :

Date_naissance=int(input("entrez votre anné de naissance :"))
age=2023-Date_naissance
print("votre age est :",+age)

#Ex3 :

largeur= float(input("Tapez la largeur de rectangle :"))
longeur= float(input("Tapez la longueur de rectangle:"))
S = largeur*longeur
P =(largeur*longeur)*2
print("La surface de rectangle est :",format(S,".2f"))
print("La périmetre de rectangle est :",format(P,".2f"))

#Ex4 :

x= int(input("veuillez entrez un nombre :"))
y= int(input("veuillez entrez un nombre:"))
p = x ** y
print("la puissance est :",+p)

#Ex5 :

x = int(input("veuillez entrez un nombre :"))
y = int(input("veuillez entrez un nombre:"))
somme = x+y
produit = x*y
différence = x-y
division = x/y
print("la somme est :",format(somme,".2f"))
print("la produit est :",+produit)
print("la différence est :",+différence)
print("la division est :",+division)

#Ex6 :

n1= float(input("veuillez entrez un nombre :"))
n2= float(input("veuillez entrez un nombre :"))  
n3= float(input("veuillez entrez un nombre :"))
n4= float(input("veuillez entrez un nombre :"))
n5= float(input("veuillez entrez un nombre :"))  
somme=n1+n2+n3+n4+n5
print("La somme est :",+somme)
moyenne=somme/5
print("La moyenne est",format(moyenne,".2f"))

#Ex7 :

import math
R = float(input("saisir le rayon de sphére : "))
V = (4*math.pi*(R**3))/3
print("Le volume d sphére est :",format(V,".2f"))

#Ex8 :

A = float(input("saisir un nombre : "))
B = float(input("saisir un nombre : "))
C = A
A = B
B = C
# A,B=B,A  يمكننا استخدام هذه الطريقة
print("la nouvelle valeur de A est :",A)
print("la nouvelle valeur de B est :",B)

#Ex9 :

T = int(input("veuillez entrez la temps :"))
H = T //3600
R = T%3600
M = R//60
S = R %60
print(H,"H:",M,"m:",S,"s")

#Ex10 :



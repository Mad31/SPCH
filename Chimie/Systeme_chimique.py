# -*- coding: utf-8 -*-
# LFT 2019 V0.1
print("Soit l'équation bilan de la réaction : ")
print("a A + b B -> c C + d D")
print("Veuillez entrez les coefficients stoechiomètriques :")
a = int(input(" Quelle est la valeur de a : "))
b = int(input(" Quelle est la valeur de b : "))
c = int(input(" Quelle est la valeur de c : "))
d = int(input(" Quelle est la valeur de d : "))
print("L'équation bilan de la réaction s'écrit donc :" )
print(a , "A + " , b  , "B -> " , c , "C + " , d  , "D")
print("Entrez maintenant en mole les quantités des réactifs A et B")
nA = float(input("Quantité de A (en mol) : "))
nB = float(input("Qauntité de B (en mol) : "))

x_maxA = nA/a
x_maxB = nB/b

if x_maxA == x_maxB :
    print("Les proportions sont stoechiométriques")
    print("Il ne reste plus de réactifs")
    print("on obtient ",c*x_maxA," mol de C")
    print("on obtient ",d*x_maxA," mol de D")
elif x_maxA < x_maxB :
    print("A est le réactif limitant")
    print("Il reste {0:7.2e} mol de B".format(nB-b*x_maxA))
    print("On obtient ",c*x_maxA," mol de C")
    print("On obtient ",d*x_maxA," mol de D")
else :
    print("B est le réactif limitant")
    print("Il reste",nA-a*x_maxB," mol de A")
    print("On obtient ",c*x_maxB," mol de C")
    print("On obtient ",d*x_maxB," mol de D")


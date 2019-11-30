# -*- coding: utf-8 -*-
# LFT 2019 V0.1

conso = float(input('Entrez la consommation de votre véhicule en L/100km : '))

n_ess = conso * 750/(114*100)

x_max = n_ess/2

m = round(x_max*8*44)

if m <= 100 :
    print("votre véhicule est de classe A")
elif 100 < m <= 120 :
    print("votre véhicule est de classe B")
elif 120 < m <= 140 :
    print("votre véhicule est de classe C")
elif 140 < m <= 160 :
    print("votre véhicule est de classe D")
elif 160 < m <= 200 :
    print("votre véhicule est de classe E")
elif 180 < m <= 250 :
    print("votre véhicule est de classe F")
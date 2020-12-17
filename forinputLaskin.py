import math

# -*- coding: utf-8 -*-T
luku1 = input('Anna ensimmäinen luku: ')
luku1 = int(luku1)
luku2 = input('Anna toinen luku: ')
luku2 = int(luku2)

valinta = 0
tulos = 0
while (valinta != 6) :
    print('(1) +\n \
    (2) -\n \
    (3) *\n \
    (4) / \n \
    (5)Vaihda luvut\n \
    (6)Lopeta')
    print('Valitut luvut: ', luku1, luku2)
    valinta = int(input('Tee valinta (1-6): '))
    if (valinta > 6 or valinta < 0):
        print('Huutista :D ')

    if (valinta == 1):
        tulos = (luku1 + luku2)
        print \
            ('Tulos on: ', tulos)
    elif (valinta == 2):
        tulos = (luku1 - luku2)
        print \
            ('Tulos on: ', tulos)
    elif (valinta == 3):
        tulos = (luku1 * luku2)
        print \
            ('Tulos on: ', tulos)
    elif (valinta == 4):
        tulos = (luku1 / luku2)
        print \
            ('Tulos on: ', tulos)
    elif (valinta == 5) :
        luku1 = input('Anna uusi ensimmäinen luku: ')
        luku1 = int(luku1)
        luku2 = input('Anna uusi toinen luku: ')
        luku2 = int(luku2)



exit(0)

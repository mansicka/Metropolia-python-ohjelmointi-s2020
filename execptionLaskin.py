##todo : tää paska looppaa!

# -*- coding: utf-8 -*-T
import math
luku1 = False
luku2 = False
valinta = False

def tarkistaluku(luku):
    try:
        luku = int(luku)
    except ValueError:
        print('Virheellinen syöte!')
        return False
    else:
        return luku




valinta = 0
tulos = 0
while True :
    while (luku1 == False):
        luku1 = input('Anna luku: ')
        luku1 = tarkistaluku(luku1)
    while (luku2 == False):
        luku2 = input('Anna luku: ')
        luku2 = tarkistaluku(luku2)

    print('(1) +\n \
    (2) -\n \
    (3) *\n \
    (4) / \n \
    (5)sin(luku1/luku2)\n \
    (6)cos(luku1/luku2) \n \
    (7)Vaihda luvut\n \
    (8)Lopeta')
    print('Valitut luvut: ', luku1, luku2)
    while valinta == False:

     valinta = input('Tee valinta (1-8): ')
     valinta = tarkistaluku(valinta)

    if (valinta > 8 or valinta < 0):
        print('Huutista :D ')
        valinta = False

    if (valinta == 1):
        tulos = (luku1 + luku2)
        print \
        ('Tulos on: ', tulos)
        valinta = False

    elif (valinta == 2):
        tulos = (luku1 - luku2)
        print \
        ('Tulos on: ', tulos)
        valinta = False

    elif (valinta == 3):
        tulos = (luku1 * luku2)
        print \
        ('Tulos on: ', tulos)
        valinta = False

    elif (valinta == 4):
        tulos = (luku1 / luku2)
        print \
        ('Tulos on: ', tulos)
        valinta = False

    elif (valinta == 5):
        tulos = math.sin(luku1/luku2)
        print \
        ('Tulos on: ', tulos)
        valinta = False

    elif (valinta == 6):
        tulos = math.cos(luku1/luku2)
        print \
        ('Tulos on: ', tulos)
        valinta = False

    elif (valinta == 7) :
            luku1 = False
            luku2 = False

            #while (luku1 == False):
             #   luku1 = input('Anna luku: ')
              #  luku1 = tarkistaluku(luku1)
            #while (luku2 == False):
             #   luku2 = input('Anna luku: ')
             #   luku2 = tarkistaluku(luku2)

            valinta = False

    elif (valinta == 8):
        break
exit(0)

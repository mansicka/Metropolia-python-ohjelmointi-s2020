# -*- coding: utf-8 -*-T

luku1 = input('Anna ensimmäinen luku: ')
luku1 = int(luku1)
luku2 = input('Anna toinen luku: ')
luku2 = int(luku2)
print('(1) +\n \
(2) -\n \
(3) *\n \
(4) /')
valinta = input('Tee valinta (1-4): ')
valinta = int(valinta)
if (valinta == 1):
    tulos = (luku1 + luku2)
elif (valinta == 2):
    tulos = (luku1 - luku2)
elif (valinta == 3):
    tulos = (luku1 * luku2)
elif (valinta == 4):
    tulos = (luku1 / luku2)
print\
    ('Tulos on: ', tulos)

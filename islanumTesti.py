# -*- coding: cp1252 -*-
tiedosto = open('merkkijonoja.txt')
rivit = tiedosto.readlines()

for i in rivit:
    sisalto = str(i[:-1])
    if sisalto.isalnum():
        print(sisalto, ' kelpaa salasanaksi.')
    else :
        print(sisalto, ' sisältää virheellisiä merkkejä.')
tiedosto.close()
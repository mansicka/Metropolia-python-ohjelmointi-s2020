# -*- coding: cp1252 -*-

import time
valinta = ''
teksti= ''

paivakirja = 'muistio.txt'
def tarkistaTiedosto(tiedosto):
    try:
        tiedosto = open(tiedosto, 'r')
        print('Käytetään muistiota: ', tiedosto.name)
        tiedosto.close()

    except IOError:
        print('Oletusmuistioa ei löydy, luodaan tiedosto.')
        tiedosto = open(tiedosto, 'w')
        print('Käytetään muistiota: ', tiedosto.name)
        tiedosto.close()

def avaaTiedosto(tiedosto):
    tiedosto = str(input('Anna tiedoston nimi: '))

    try:
        tiedosto = open(tiedosto, 'r')
        print('Käytetään muistiota: ', tiedosto.name)
        tiedosto.close()
        return tiedosto.name
    except IOError:
        print('Tiedostoa ei löydy, luodaan tiedosto.')
        tiedosto = open(tiedosto, 'w')
        return tiedosto.name
        tiedosto.close()


#menu
def menu():
    print('(1) Lue muistikirjaa\n \
    (2) Lisää merkintä\n \
    (3) Tyhjennä muistikirja\n \
    (4) Vaihda muistiota\n \
    (5) Lopeta')

#Lue tiedosto
def readAndReturn(muisto):
    while True:
        try:
        muistio = open(muisto,'rb')
        list = pickle.load(muistio)


        muistio.close()

        except IOError:


#Kirjoita tiedostoon
def write(paivakirja, teksti):
  try:
    teksti = teksti
    tiedosto = open(paivakirja,'a')
    tiedosto.write(teksti)
    tiedosto.write(':::')
    tiedosto.write(time.strftime("%e/%m/%C"))
    tiedosto.write('\n')
    tiedosto.close()
  except IOError:
    return False


# Menu
tarkistaTiedosto(paivakirja)
menu()
try:
  valinta = int(input('Mitä haluat tehdä?: '))
# valinnat

  while (valinta != 5) :
    if (valinta < 1 or valinta > 5):
     print('Virheellinen valinta!')
     tarkistaTiedosto(paivakirja)
     menu()
     valinta = int(input('Mitä haluat tehdä?: '))

    elif (valinta == 1) :
     print(readAndReturn(paivakirja))
     tarkistaTiedosto(paivakirja)
     menu()
     valinta = int(input('Mitä haluat tehdä?: '))

    elif (valinta == 2) :
     teksti = input('Kirjoita uusi merkintä: ')
     write(paivakirja, teksti)
     tarkistaTiedosto(paivakirja)
     menu()
     valinta = int(input('Mitä haluat tehdä?: '))

    elif (valinta == 3) :
        open(paivakirja, 'w').close()
        print('Muistio tyhjennetty.')
        tarkistaTiedosto(paivakirja)
        menu()
        valinta = int(input('Mitä haluat tehdä?: '))

    elif (valinta == 4):
        paivakirja = avaaTiedosto(paivakirja)
        tarkistaTiedosto(paivakirja)
        menu()
        valinta = int(input('Mitä haluat tehdä?: '))

except ValueError:
    print('Virheellinen valinta!')
print('Lopetetaan.')
exit(0)

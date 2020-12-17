# -*- coding: cp1252 -*-
def readAndReturn(tiedosto):
  try:
    tiedosto = open(tiedosto,'r')
    sisus = tiedosto.read()
    tiedosto.close()
    sisus = int(sisus)
    palautus = sisus + 313

  except ValueError:
      print('Tiedoston sisältö virheellinen!')
  except IOError:
      print('Virheellinen tiedostonnimi')
  else:
      return print('Saatiin tulos ', palautus)


if __name__ == '__main__':
    readAndReturn(input('Anna tiedoston nimi: '))

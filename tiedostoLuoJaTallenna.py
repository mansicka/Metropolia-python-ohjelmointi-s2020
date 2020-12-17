# -*- coding: cp1252 -*-
tiedostonimi = input('Minkäniminen tiedosto luodaan?:')
teksti = input('Mitä kirjoitetaan tiedostoon?:')

tiedosto = f = open(tiedostonimi, 'w')
tiedosto.write(teksti)

print('Luotiin tiedosto ',tiedosto.name, ' ja siihen tallennettiin teksti: ', teksti)

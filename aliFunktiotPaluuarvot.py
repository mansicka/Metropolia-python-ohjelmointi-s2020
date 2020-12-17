# -*- coding: cp1252 -*-
def pituusmitta(sana) :
    pituus = int(len(sana))
    return pituus

if __name__ == "__main__":

    syote = ''
    while syote != 'Lopeta':
        syote = input('Anna syöte (Lopeta lopettaa): ')
        if syote == 'Lopeta':
            break
        elif (len(syote) > 0):
         print('Antamasi syöte oli', pituusmitta(syote), 'merkkiä pitkä.')
        else:
            print('Et antanut syötettä')
    exit(0)


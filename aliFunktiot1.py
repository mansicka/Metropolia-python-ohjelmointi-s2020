# -*- coding: cp1252 -*-

def pitkasana(sana):

        if sana == 'Lopeta' :
            exit(0)

        elif len(sana) > 5:
         return(sana)

        else :
         return('Oletustulostus')


if __name__ == "__main__":
    sana = ''
    while sana != 'Lopeta':
        sana = str(input('Anna syöte (Lopeta lopettaa): '))
        sana = pitkasana(sana)
        print(sana)

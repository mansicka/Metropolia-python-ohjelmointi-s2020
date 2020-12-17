un = 'Erkki'
pw = 'Esimerkki'

syote = input('Anna nimi: ')
if (syote == un) :
    syote = input('Anna salasana: ')
    if (syote == pw) :
        print('Salasana ja nimi oli oikein!')
    else : print('Salasana oli väärin.')
else: print('Nimi oli väärin.')

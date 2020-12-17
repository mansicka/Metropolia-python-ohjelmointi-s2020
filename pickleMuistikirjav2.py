# -*- coding: cp1252 -*-
import time
import pickle
def fileCheck(muistio, lista):
    try:
        muistio = open(muistio, 'r')
        print('Käytetään muistiota: ', muistio.name)
        muistio.close()

    except IOError:
        print('Virhe tiedostossa, luodaan uusi muistio.dat.')
        file = open(muistio, 'wb')
        pickle.dump(lista, file)
        file.close()


def dat2List(muistio):
    while True:
        try:
            file = open(muistio, "rb")
            data = pickle.load(file)
            list = [line.rstrip('\n') for line in data]
            file.close()
            return list
        except EOFError:
            break


def add(lista):
    try:
        add = input('Kirjoita uusi merkintä: ')
        add = add + ':::' + time.strftime("%e/%m/%C")
        lista.append(add)

    except ValueError:
        print('Virhe')

def delete(lista):
    print('Listalla on ', len(lista), ' merkintää.')
    try:
        delete = int(input('Mitä niistä poistetaan?: '))
        delete = delete - 1
        deleted = lista.pop(delete)
        print('Poistettiin merkintä ', deleted)
    except IndexError:
        print('Virheellinen valinta.')

def modify(lista):
    print('Listalla on ', len(lista), ' merkintää.')
    try:
        i = int(input('Mitä niistä muutetaan?: '))
        i = i - 1
        print(lista[i])
        text = str(input('Anna uusi teksti: ')) + ':::' + time.strftime("%e/%m/%C")
        lista[i] = text
    except ValueError:
        print('Virhe')

def saveAndCloselist(list, muistio):
    file = open(muistio,'wb')
    pickle.dump(list, file)
    file.close()
    print('Lopetetaan.')
    exit(0)

menu = '(1) Lue muistikirjaa\n \
    (2) Lisää merkintä\n \
    (3) Muokkaa merkintää\n \
    (4) Poista merkintä\n \
    (5) Tallenna ja lopeta \n \n \
    Mitä haluat tehdä?: '

#########################
def main():
    lista = []
    muistio = 'muistio.dat'
    fileCheck(muistio, lista)
########################
    while True:
        try:
            select = int(input(menu))

            if (select > 6 or select < 0):
                print('Virheellinen valinta.')

            elif select == 1:
                for i in lista:
                    print(i)

            elif select == 2:
                add(lista)

            elif select == 3:
                modify(lista)

            elif select == 4:
                delete(lista)

            elif select == 5:
                saveAndCloselist(lista, muistio)

        except ValueError:
            print('Virheellinen valinta.')


if __name__ == '__main__':
    main()

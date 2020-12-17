# -*- coding: cp1252 -*-
import time
import pickle
#

#
def dat2List(muistio):
    while True:
        try:
            file = open(muistio, "rb")
            data = pickle.load(file)
            list = [line.rstrip('\n') for line in data]
            print(list)
            return list
        except EOFError:
            break

def fileCheck(muistio):
    try:
        muistio = open(muistio, 'r')
        #print('Käytetään muistiota: ', tiedosto.name)
        muistio.close()

    except IOError:
        print('Virhe tiedostossa, luodaan uusi muistio.dat.')
        muistio = open(muistio, 'w')
        muistio.close()


def saveAndCloselist(list, muistio):
    print('Lopetetaan.')
    muistio = open(muistio,'ab')
    pickle.load(muistio)
    pickle.dump(list, muistio)
    list.close()


def add(list):
    try:
        add = input('Mitä lisätään?: ')
        list.append(add)
    except ValueError:
        print('Virhe')

def modifyItem(list):
    print('Listalla on ', len(list), ' merkintää.')
    i = int(input('Mitä niistä muutetaan?:'))
    while True:
        try:
            if (i > len(list)):
                print('Virhe!')
            else:
                text = str(input('Anna uusi teksti: '))
                text = text + ':::' + time.strftime("%e/%m/%C")
                list[i] = text
                return list
        except ValueError:
            print('Virhe!')

def menu():
    print('(1) Lue muistikirjaa\n \
    (2) Lisää merkintä\n \
    (3) Muokkaa merkintää\n \
    (4) Poista merkintä\n \
    (5) Tallenna ja lopeta')

def menuSelector():
    while True:
        try:
            selection = int(input("Mitä haluat tehdä?: "))
            return selection
        except Exception:
            print("Virheellinen valinta!")

def printList(list):
        for i in list:
            print(i)

def main():
    list = []
    muistio = 'muistio.dat'

    fileCheck(muistio)
    list = dat2List(muistio)
    menu()
    selection = menuSelector()

    while True:
        ###valikon toiminnat
        #
        if selection == 1:
            try:
                for i in list:
                    print(i)
                menu()
                selection = menuSelector()

            except TypeError:
                menu()
                selection = menuSelector()

        #
        elif selection == 2:
            list = add(list)
            menu()
            selection = menuSelector()




if __name__ == '__main__':

    main()

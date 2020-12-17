# -*- coding: cp1252 -*-
def add(lista):
    try:
        add = input('Mitä lisätään?: ')
        lista.append(add)

    except ValueError:
        print('Virhe')

def delete(lista):
    print('Listalla on ', len(lista), ' alkiota.')
    try:
        delete = int(input('Monesko niistä poistetaan?: '))
        lista.pop(delete)
    except IndexError:
        print('Virheellinen valinta.')

def end(lista):
    print('Listalla oli tuotteet:')
    for i in lista:
        print(i)
    exit(0)

menu = '\
    Haluatko\n \
    (1)Lisätä listaan\n \
    (2)Poistaa listalta vai\n \
    (3)Lopettaa?:'

#########################
def main():
    lista = []

    while True:
        try:
            select = int(input(menu))

            if (select > 3 or select < 0):
                print('Virheellinen valinta.')

            elif select == 1:
                add(lista)

            elif select == 2:
                delete(lista)

            elif select == 3:
                end(lista)

            elif select == 4:
                for i in lista:
                    print(i)


        except Valuerror:
            print('Virheellinen valinta.')


if __name__ == '__main__':
    main()

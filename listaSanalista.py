# -*- coding: cp1252 -*-


def txt2List(file):
    try:
        list = [line.rstrip('\n') for line in open(file)]
        list = sorted(list)
        print('Sanat laitettuna aakkosjärjestykseen:')
        for i in list:
            print(i)

    except IOError:
        print('Virhe')


def main():
    file = 'sanoja.txt'
    txt2List(file)


if __name__ == '__main__':
    main()

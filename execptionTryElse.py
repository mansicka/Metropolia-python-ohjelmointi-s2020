# -*- coding: cp1252 -*-
def main():
    try:
        syote = int(input('Anna luku: '))
    except Exception:
        print('Virheellinen syöte!)
    else:
        print('Syöte oli kelvollinen.')

if __name__ == '__main__':
    main()


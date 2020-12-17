# -*- coding: cp1252 -*-
def testaa(sana):

    if (len(sana) < 5 or sana.isdigit() == True or sana.isalpha() == True) :
        return False
#
    else:
        return True


if __name__ == "__main__":
    while True:
     testattava = input("Anna testattava sana: ")
     tulos = testaa(testattava)
     if tulos == True:
          print("Antamasi sana kelpaa salasanaksi!")

     else :
        print("Sana ei kelpaa.")

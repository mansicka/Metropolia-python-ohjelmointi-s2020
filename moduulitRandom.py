# -*- coding: cp1252 -*-
import random

if __name__ == "__main__":
    print('Heitetään kolikkoa viidesti:')
    i = int()
    while i < 5:
        kolikko = random.randint(0,1)
        i = i + 1
        if kolikko == 1:
             print('Kruuna!')
        else:
             print('Klaava!')

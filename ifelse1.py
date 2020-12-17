luku = input('Anna luku: ')
luku2 = input('Anna toinen luku: ')
luku = int(luku)
luku2 = int(luku2)

if (luku % 2 == 0) and (luku2 % 2 == 0):
    print('Molemmat luvut ovat parillisia.')
elif (luku % 2 == 0) or (luku2 % 2 == 0):
    print('Toinen luku on parillinen.')
else:
    print('Molemmat luvut ovat parittomia.')

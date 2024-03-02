from math import sqrt
x1 = int(input('Unesite prvu koordinatu tacke A: '))
y1 = int(input('Unesite drugu koordinatu tacke A: '))
x2 = int(input('Unesite prvu koordinatu tacke B: '))
y2 = int(input('Unesite drugu koordinatu tacke B: '))

rastojanje = sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))

print(f'Euklidovo rastojanje izmedju tacke A i B je {round(rastojanje, 2)}')

from math import sqrt
x1 = int(input('Unesite prvu kordinat prve tacke: '))
y1 = int(input('Unesite drugu kordinat prve tacke: '))
x2 = int(input('Unesite prvu kordinat druge tacke: '))
y2 = int(input('Unesite drugu kordinat druge tacke: '))

x3 = (x1+x2)/2
y3 = (y1+y2)/2

print(f'Kordinate lokacije su x = {x3} i y = {y3}')
print(f'Rastojanje od prve tacke odnosno druge tacke do destinacije je {round(sqrt(pow(x1-x3, 2)+pow(y1-y3, 2)), 2)}')

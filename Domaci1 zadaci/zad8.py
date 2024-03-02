from math import sqrt
PI = 3.14159
povrsina = float(input('Unesite povrsina stonjaka: '))
precnik = sqrt(povrsina/PI)
obim = 2*precnik*PI
print(f'Potrebna duzina trake za ivicu stonjaka je: {round(obim, 2)}')

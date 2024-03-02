d = float(input('Unesite duzinu terena u metrima: '))
s = float(input('Unesite sirina terena u metrima: '))
r = float(input('Unesite razdaljinu ograde od terena u metrima: '))

s += r
d += r
obim = 2 * (s+d)

print(f'Duzina ograde je: {obim} metara')

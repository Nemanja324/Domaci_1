broj = input('Unesite cetvorocifreni broj: ')
if len(broj) == 4:
    broj = int(broj)
    suma = 0
    while broj > 0:
        cif = broj % 10
        suma += cif
        broj //= 10
    print(f'Kvadrat zbira cifara je: {pow(suma, 2)}')
else:
    print('Niste unijeli cetvorocifreni broj, probajte ponovo.')

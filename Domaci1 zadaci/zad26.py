broj = input('Unesite cetvorocifreni broj: ')
if len(broj) == 4:
    print(f'Stan se nalazi na {int(broj[2])}. spratu')
else:
    print('Niste unijeli cetvorocifreni broj, probajte ponovo.')

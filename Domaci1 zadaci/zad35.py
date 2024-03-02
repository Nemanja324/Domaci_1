broj = input('Unesite petocifreni broj: ')
if len(broj) == 5:
    print(f'Stan se nalazi na {int(broj[2])+int(broj[4])}. spratu')
else:
    print('Niste unijeli petocifreni broj, probajte ponovo.')

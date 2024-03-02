broj = input('Unesite trocifren broj: ')
if len(broj) == 3:
    print(f'Unijeti broj prije zamjene {int(broj)}, nakon zamjene {int(broj[::-1])}')
else:
    print('Niste unijeli trocifren broj, probajte ponovo.')

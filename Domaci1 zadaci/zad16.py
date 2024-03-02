kilometri = float(input('Unesite koliko je kilometara presao taksi: '))

cijena = 1

if kilometri <= 1:
    print(f'Cijena voznje je: {cijena}€')
else:
    cijena += (kilometri-1)*0.5
    print(f'Cijena voznje je: {cijena}€')

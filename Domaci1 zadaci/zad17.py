cijena_knjige = float(input('Koliko kosta knjiga?$ '))
popust = int(input('Koliki je popust knjiga: '))

finalna_cijena = cijena_knjige - cijena_knjige * (popust/100)

print(f'Finalna cijena je: ${finalna_cijena}')

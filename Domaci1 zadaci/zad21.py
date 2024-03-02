
broj = input('Unesite cetvorocifreni broj: ')
if len(broj) == 4:
    prva = int(broj[0])
    druga = int(broj[1])
    treca = int(broj[2])
    cetvrta = int(broj[3])

    raz_kvadrata = (druga - treca) * (druga + treca)
    kvadrat_zbir = pow(prva, 2) + 2*prva*cetvrta + pow(cetvrta, 2)
    print(f'Sifra je: {kvadrat_zbir - raz_kvadrata}')
else:
    print('Niste unijeli cetvorocifreni broj, probajte ponovo.')

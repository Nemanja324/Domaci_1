
def suma(pom):
    kvadrirana_suma = 0
    while pom > 0:
        cif = pom % 10
        kvadrirana_suma += cif
        pom = pom // 10
    kvadrirana_suma = pow(kvadrirana_suma, 2)
    return kvadrirana_suma


broj = input('Unesite sestocifren broj: ')
if len(broj) == 6:
    proizvod = int(broj[2]) * int(broj[3])
    broj = int(broj)
    print(f'Identifikacioni broj je: {suma(broj)-proizvod}')
else:
    print('Niste unijeli sestocifren broj, probajte ponovo.')

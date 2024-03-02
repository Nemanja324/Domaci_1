def zbir(broj1):
    suma = 0
    while broj1 > 0:
        cif = broj1 % 10
        suma += cif
        broj1 = broj1 // 10
    return suma


def proizvod(broj1):
    p = 1
    while broj1 > 0:
        cif = broj1 % 10
        p *= cif
        broj1 = broj1 // 10
    return p


broj = int(input('Unesite poznati trocifreni broj: '))

print(f'Sifra od vrata je: {proizvod(broj)-zbir(broj)}')



def zbir(broj):
    suma = 0
    while broj > 0:
        cif = broj % 10
        suma += cif
        broj = broj // 10
    return suma


neki_broj = input('Unesite neki broj: ')
if len(neki_broj) == 3:
    neki_broj = int(neki_broj)
    print(zbir(neki_broj))
elif len(neki_broj) == 4 and neki_broj[0] == '-':
    neki_broj = int(neki_broj)
    neki_broj = abs(neki_broj)
    print(zbir(neki_broj))
else:
    print('Niste unijeli trocifreni broj.')

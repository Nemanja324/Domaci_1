a = float(input('Unesite vrijednost od konstante \'a\': '))
b = float(input('Unesite vrijednost od konstante \'b\': '))
c = float(input('Unesite vrijednost od konstante \'c\': '))

resenje = pow(a, 2) + pow(b, 2) + pow(c, 2) + 2*a*b + 2*a*c + 2*b*c

print(f'Resenje kvadrata trinoma je: {resenje}')

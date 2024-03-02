from math import sqrt

a = float(input('Unesite vrijednost od konstante \'a\': '))
b = float(input('Unesite vrijednost od konstante \'b\': '))
c = float(input('Unesite vrijednost od konstante \'c\': '))
# Slucaj kad je kvadratna jednacina potpuna
if b != 0 and c != 0:
    if pow(b, 2)-4*a*c >= 0:
        x1 = (-b-sqrt(pow(b, 2)-4*a*c))/2*a
        x2 = (-b+sqrt(pow(b, 2)-4*a*c))/2*a
        print(f'Resenja kvadratne jednacine su x1= {round(x1, 2)} i x2= {round(x2, 2)}')
    else:
        print(f'Podkorijena vrijednost je negativna!')
# Slucaj kad je kvadratna jednacina nepotuna
elif c == 0 and b == 0:
    x1 = x2 = 0
    print(f'Resenja kvadratne jednacine su x1= {x1} i x2= {x2}')
elif b == 0:
    x1 = +(sqrt(-c/a))
    x2 = -(sqrt(-c/a))
    print(f'Resenja kvadratne jednacine su x1= {round(x1, 2)} i x2= {round(x2, 2)}')
elif c == 0:
    x = -(b/a)
    print(f'Resenje kvadratne jednacine je x= {round(x, 2)}')

broj = input('Unesite sestocifren broj: ')
if len(broj) == 6:
    a = int(broj[0])
    b = int(broj[1])
    c = int(broj[2])
    d = int(broj[3])
    e = int(broj[4])
    f = int(broj[5])
    if a*c+2+f == b+d*e:
        print(True)
    else:
        print(False)

else:
    print('Niste unijeli sestocifren broj, probajte ponovo.')

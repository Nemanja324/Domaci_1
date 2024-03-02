
N = int(input('Unesite broj ucenika na obije strane: '))
K = int(input('Unesite broj ucenika na drugoj strani: '))
p1 = float(input('Unesite prosječan broj poena učenika na prvoj strani: '))
p2 = float(input('Unesite prosječan broj poena učenika na drugoj strani: '))

br_ucenika_str_1 = N-K

ukupna_zbir_ocjena = br_ucenika_str_1*p1 + K*p2

ukupna_prosjecna_ocjena = round(ukupna_zbir_ocjena/N, 2)

print(f'Ukupna prosjeca ocjena je {ukupna_prosjecna_ocjena}')

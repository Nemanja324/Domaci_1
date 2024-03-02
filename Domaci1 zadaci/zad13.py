from math import sqrt
def moduo(x1,y1,x2,y2):
  x = x1-x2
  y = y1-y2
  return round(sqrt(x*x+y*y), 3)

stari_hrast = []
kordinate = input('Unesite kordinate starog hrasta: ')
stari_hrast = kordinate.split()
stara_kuca = []
kordinate = input('Unesite kordinate stare kuce: ')
stara_kuca = kordinate.split()

for i in range(0, len(stara_kuca)):
  stara_kuca[i] = int(stara_kuca[i])
for i in range(0, len(stari_hrast)):
  stari_hrast[i] = int(stari_hrast[i])

kordinate_blaga = []
kordinate_blaga.append(stara_kuca[0]+2)
kordinate_blaga.append(stara_kuca[1]-3)
print(f'Kordinate blaga su {kordinate_blaga}')
print(f'Vazdusno rastojanje od hrasta do blaga je {moduo(stari_hrast[0],stari_hrast[1],kordinate_blaga[0],kordinate_blaga[1])}')
print(f'Rastojanje od hrasta do kuce pa do blaga je {round(moduo(stari_hrast[0],stari_hrast[1],stara_kuca[0],stara_kuca[1]) + moduo(stara_kuca[0],stara_kuca[1],kordinate_blaga[0],kordinate_blaga[1]), 3)}')
print(stari_hrast)
print(stara_kuca)
print(kordinate_blaga)
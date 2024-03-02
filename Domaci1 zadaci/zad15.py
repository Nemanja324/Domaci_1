from math import sqrt
A_x = int(input('Unesite prvu koordinatu tacke A: '))
A_y = int(input('Unesite drugu koordinatu tacke A: '))
B_x = int(input('Unesite prvu koordinatu tacke B: '))
B_y = int(input('Unesite drugu koordinatu tacke B: '))
C_x = int(input('Unesite prvu koordinatu tacke C: '))
C_y = int(input('Unesite drugu koordinatu tacke C: '))
x1 = A_x - B_x
y1 = A_y - B_y
x2 = B_x - C_x
y2 = B_y - C_y
x3 = A_x - C_x
y3 = A_y - C_y
A = sqrt(pow(x1, 2)+pow(y1, 2))
B = sqrt(pow(x2, 2)+pow(y2, 2))
C = sqrt(pow(x3, 2)+pow(y3, 2))
S = (A+B+C)/2
povrsina = sqrt(S*(S-A)*(S-B)*(S-C))
print(f'Povrsina trougla je: {povrsina}')

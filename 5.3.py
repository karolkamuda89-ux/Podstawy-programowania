a= input('wprowadź długość boku a :')
b= input('wprowadź długość boku b :')
c= input('wprowadź wysokość:')
bok_a = int(a)
bok_b = int(b)
bok_c = int(c)
Objetosc = bok_a * bok_b * bok_c
pole_powierzchni_calkowitej = (bok_a * bok_b) * 2 + (bok_a * bok_c) * 2 + (bok_b * bok_c) * 2
print(F'objętość wynosi {Objetosc} a pole powierzchni całkowitej wynosi {pole_powierzchni_calkowitej}')
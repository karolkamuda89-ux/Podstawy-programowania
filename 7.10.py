import random
rzut_komputer =  int(random.randint(1,6))
liczba_uzytkownika = int(input('Podaj liczbe od 1 - 6 : '))
wynik = rzut_komputer == liczba_uzytkownika
print(f'Wygrałes : {wynik}')
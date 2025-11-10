rejstracja = input('Podaj rejstracje:')
krakow = rejstracja[0:2] == 'KK' or rejstracja == 'KR'
print(f'car is from krakow : {krakow}')
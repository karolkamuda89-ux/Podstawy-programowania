cena = input('podaj cene:')
rabat = input('podaj rabat:')
cena = float(cena)
rabat = float(rabat)
cena_po_obnizce = cena * rabat
print(f'cena przed obnizka wynosi{cena:.2f} a po obniżce {cena_po_obnizce:.2f}')
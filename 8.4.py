CM_NA_INCH = 2.54
cm = int(input('podaj wzrost w cm: '))
cale_total = int(cm / CM_NA_INCH)
stopy = cale_total // 12
cale_poprawne = cale_total % 12

print(f'mam {cm} cm wzrostu, czyli {stopy} stóp i {cale_poprawne} cali')
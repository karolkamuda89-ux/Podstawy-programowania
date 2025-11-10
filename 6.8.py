first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_letters = last_letter_code - first_letter_code - 1
if first_letter_code == last_letter_code:
    print(0)
else :
    print(f'beetwen {first} and {last} is {number_letters}')

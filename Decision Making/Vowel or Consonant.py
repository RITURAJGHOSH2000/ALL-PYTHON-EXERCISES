from tkinter import N


alphabet = input('Enter an alphabet of your choice: ')
if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u' or alphabet == 'A' or alphabet == 'E' or alphabet == 'I' or alphabet == 'O' or alphabet == 'U':
    print(f'Your entered alphabet is \'{alphabet}\' which is a vowel')
elif alphabet == 'y' or alphabet == 'Y':
    print(
        f'Sometimes \'{alphabet}\' is a vowel, and sometimes \'{alphabet}\' is a consonant')
else:
    print(f'Your entered alphabet is \'{alphabet}\' which is a consonant')

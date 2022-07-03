print('\nThe following table lists an octave of music notes, beginning with middle C, along with the frequencies:-\n')
print('\t\t----------------------------------------')
print('\t\t Note                     Frequency(Hz)')
print('\t\t----------------------------------------')
print('\t\t  C4                         261.63')
print('\t\t  D4                         293.66')
print('\t\t  E4                         329.63')
print('\t\t  F4                         349.23')
print('\t\t  G4                         392.00')
print('\t\t  A4                         440.00')
print('\t\t  B4                         493.88')
name = input('\nEnter the name of the note from the above mentioned list: ')
note = name[0]
octave = int(name[1])
if note == 'C':
    freq = 261.63
elif note == 'D':
    freq = 293.66
elif note == 'E':
    freq = 329.63
elif note == 'F':
    freq = 349.23
elif note == 'G':
    freq = 392.00
elif note == 'A':
    freq = 440.00
elif note == 'B':
    freq = 493.88
freq = freq / (2 ** (4 - octave))
print(f'The frequency of {name} is {freq}')

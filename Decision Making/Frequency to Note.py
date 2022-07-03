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
freq = float(
    input('\nEnter the frequency of the note from the above mentioned list: '))
if freq == 261.63:
    print('The name of the note is C4')
elif freq == 293.66:
    print('The name of the note is D4')
elif freq == 329.63:
    print('The name of the note is E4')
elif freq == 349.23:
    print('The name of the note is F4')
elif freq == 392.00:
    print('The name of the note is G4')
elif freq == 440.00:
    print('The name of the note is A4')
elif freq == 493.88:
    print('The name of the note is B4')
else:
    print('The entered frequency is not in the list')

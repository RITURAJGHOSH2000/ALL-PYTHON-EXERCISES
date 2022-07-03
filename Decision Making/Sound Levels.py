print('\nThe following table lists the sound level in decibels for several common noises:-\n')
print('\t\t----------------------------------------')
print('\t\t Noise            |       Decibel Level')
print('\t\t----------------------------------------')
print('\t\tJackhammer        |          130 dB')
print('\t\tGas Lawnmower     |          106 dB')
print('\t\tAlarm Clock       |          70 dB')
print('\t\tQuiet Room        |          40 dB')
print('\t\t----------------------------------------\n')
dB = int(input('Enter the noise level (in dB): '))
if dB == 130:
    print(f'{dB}dB noise level is made by Jackhammer')
if dB == 106:
    print(f'{dB}dB noise level is made by Gas Lawnmower')
if dB == 70:
    print(f'{dB}dB noise level is made by Alarm Clock')
if dB == 40:
    print(f'{dB}dB noise level of Quiet Room')
if dB > 40 and dB < 70:
    print(f'{dB}dB noise level is in between the sound made by Quiet Room and Alarm Clock')
if dB > 70 and dB < 106:
    print(f'{dB}dB noise level is in between the sound made by Alarm Clock and Gas Lawnmower')
if dB > 106 and dB < 130:
    print(f'{dB}dB noise level is in between the sound made by Gas Lawnmower and Jackhammer')
elif dB > 130:
    print(f'{dB}dB is higher than the highest noise level mentioned in the list, so cannot mention the range in between which two objects noise level it comes. But one thing can be commented that the object is even louder than a Jackhammer')
elif dB < 40:
    print(f'{dB}dB is smaller than the smallest noise level mentioned in the list, so cannot mention the range in between which two objects the noise level it comes. But one thing can be commented that the object is even quieter than a Quiet Room')

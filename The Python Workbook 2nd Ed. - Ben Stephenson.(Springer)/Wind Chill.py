Ta = int(input('Enter the air temperature (in °C): '))
V = float(input('Enter the wind speed (in kmph): '))
if Ta <= 10 and V > 4.8:
    WCI = 13.12 + (0.6215 * Ta) - (11.37 * (V ** 0.16)) + \
        (0.3965 * Ta * (V ** 0.16))
    WCI_format = "{:.2f}".format(WCI)
    print(f'The Wind Chill Index is: {WCI_format}')
if Ta > 10:
    print(
        f'You have entered air temperature of {Ta}°C which is above 10°C. So, the Wind Chill Index cannot be calculated, please enter the air temperature below 10°C')
if V < 4.8:
    print(
        f'You have entered wind speed of {V}kmph which is less than 4.8kmph. So, the Wind Chill Index cannot be calculated, please enter the wind speed above 4.8kmph')

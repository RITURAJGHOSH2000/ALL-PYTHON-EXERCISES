from random import randrange
v = randrange(0, 38)
if v == 37:
    print('The spin resulted is 00....')
else:
    print(f'The spin resulted is {v}')
if v == 37:
    print('Pay 00')
else:
    print(f'Pay {v}')
if v % 2 == 1 and v >= 1 and v <= 9 or v % 2 == 0 and v >= 12 and v <= 18 or v % 2 == 1 and v >= 19 and v <= 27 or v % 2 == 0 and v >= 30 and v <= 36:
    print("Pay Red")
elif v == 0 or v == 37:
    pass
else:
    print("Pay Black")
if v >= 1 and v <= 36:
    if v % 2 == 1:
        print("Pay Odd")
    else:
        print("Pay Even")
if v >= 1 and v <= 18:
    print("Pay 1 to 18")
elif v >= 19 and v <= 36:
    print("Pay 19 to 36")

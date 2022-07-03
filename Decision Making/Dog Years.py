hy = int(input('Enter number of human years: '))
if hy < 3 and hy > 0:
    dy1 = hy * 10.5
    print(f'The equivalent dog years for {hy} human years is {dy1}')
if hy >= 3:
    dy2 = (2 * 10.5) + ((hy - 2) * 4)
    print(f'The equivalent dog years for {hy} human years is {dy2}')
elif hy < 0:
    print('You have entered a negative number. So, can\'t show the number of dog years, as years cannot be in negative')

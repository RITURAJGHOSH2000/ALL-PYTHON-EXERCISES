y = int(input('Enter year: '))
m = int(input('Enter month: '))
d = int(input('Enter day: '))
if d <= 31 and m <= 12:
    if m == 2 and y % 4 == 0 and d == 29:
        m += 1
        d = 1
        print(f'The next day is: {y}-{m}-{d}')
    elif d > 29 and d <= 31:
        print('February doesn\'t have more than 29 days in a leap year')
    elif m == 2 and y % 4 != 0 and d == 28:
        m += 1
        d = 1
        print(f'The next day is: {y}-{m}-{d}')
    elif d > 28 and d <= 31:
        print('February doesn\'t have more than 28 days in a non-leap year')
    elif d >= 1 and d < 30:
        d = d + 1
        print(f'The next day is: {y}-{m}-{d}')
    elif (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10) and d == 31:
        d = 1
        m += 1
        print(f'The next day is: {y}-{m}-{d}')
    elif (m == 4 or m == 6 or m == 9 or m == 11) and d == 30:
        d = 1
        m += 1
        print(f'The next day is: {y}-{m}-{d}')
    elif m == 12 and d == 31:
        y += 1
        m = 1
        d = 1
        print(f'The next day is: {y}-{m}-{d}')
    elif d > 31:
        print('Days cannot be more than 31')
    elif m > 12:
        print('Months cannot be more than 12')
elif d > 31 and m <= 12:
    print('No month has more than 31 days')
elif m > 12 and d <= 31:
    print('No year has more than 12 months')
else:
    print('Please check the day and month value which you entered as they are above 31 and 12')

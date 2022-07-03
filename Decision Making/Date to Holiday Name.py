print('\nThe following table consists of the National Holidays that comes on the same date every year:-\n')
print('\t\t-----------------------------------------')
print('\t\t   Holiday                       Date')
print('\t\t-----------------------------------------')
print('\t\tNew Year\'s Day                 January 1')
print('\t\tCanada Day                     July 1')
print('\t\tChristmas Day                  December 25')
m = input('\nEnter the month: ')
d = int(input('Enter the date: '))
if m == 'January' and d == 1:
    print(f'The name of the holiday in Canada on {m} {d} is New Year\'s Day')
elif m == 'July' and d == 1:
    print(f'The name of the holiday in Canada on {m} {d} is Canada Day')
elif m == 'December' and d == 25:
    print(f'The name of the holiday in Canada on {m} {d} is Christmas Day')
else:
    print(f'The entered month {m} and date {d} is not in the list')

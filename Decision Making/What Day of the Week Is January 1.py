from math import floor
y = int(input('Enter the year: '))
d = int((y + floor((y - 1) / 4) - floor((y - 1) / 100) + floor((y - 1) / 400)) % 7)
if d == 0:
    print(f'The day of the week for January 1 of the year {y} is Sunday')
elif d == 1:
    print(f'The day of the week for January 1 of the year {y} is Monday')
elif d == 2:
    print(f'The day of the week for January 1 of the year {y} is Tuesday')
elif d == 3:
    print(f'The day of the week for January 1 of the year {y} is Wednesday')
elif d == 4:
    print(f'The day of the week for January 1 of the year {y} is Thursday')
elif d == 5:
    print(f'The day of the week for January 1 of the year {y} is Friday')
elif d == 6:
    print(f'The day of the week for January 1 of the year {y} is Saturday')

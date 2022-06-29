days = int(input('Enter the number of day(s): '))
hours = int(input('Enter the number of hour(s): '))
mins = int(input('Enter the number of minute(s): '))
secs = int(input('Enter the number of second(s): '))
n_secs = (86400 * days) + (3600 * hours) + (60 * mins) + secs
print(
    f'The number of seconds in {days} days, {hours} hours, {mins} minutes and {secs} seconds are {n_secs} s')

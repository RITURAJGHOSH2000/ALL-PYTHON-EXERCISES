g = input('Enter the letter grade: ')
if g == 'A+' or g == 'A':
    print(f'The equivalent grade point for the letter grade {g} is 4.0')
elif g == 'A-':
    print(f'The equivalent grade point for the letter grade {g} is 3.7')
elif g == 'B+':
    print(f'The equivalent grade point for the letter grade {g} is 3.3')
elif g == 'B':
    print(f'The equivalent grade point for the letter grade {g} is 3.0')
elif g == 'B-':
    print(f'The equivalent grade point for the letter grade {g} is 2.7')
elif g == 'C+':
    print(f'The equivalent grade point for the letter grade {g} is 2.3')
elif g == 'C':
    print(f'The equivalent grade point for the letter grade {g} is 2.0')
elif g == 'C-':
    print(f'The equivalent grade point for the letter grade {g} is 1.7')
elif g == 'D+':
    print(f'The equivalent grade point for the letter grade {g} is 1.3')
elif g == 'D':
    print(f'The equivalent grade point for the letter grade {g} is 1.0')
elif g == 'F':
    print(f'The equivalent grade point for the letter grade {g} is 0')
else:
    print(f'The equivalent grade point for the letter grade {g} is not known')

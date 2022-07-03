gp = float(input('Enter the grade point: '))
if gp >= 4.0:
    print(f'The equivalent letter grade for the grade point {gp} is A+')
elif gp == 4.0:
    print(f'The equivalent letter grade for the grade point {gp} is A')
elif gp < 4.0 and gp >= 3.7:
    print(f'The equivalent letter grade for the grade point {gp} is A-')
elif gp < 3.7 and gp >= 3.3:
    print(f'The equivalent letter grade for the grade point {gp} is B+')
elif gp < 3.3 and gp >= 3.0:
    print(f'The equivalent letter grade for the grade point {gp} is B')
elif gp < 3.0 and gp >= 2.7:
    print(f'The equivalent letter grade for the grade point {gp} is B-')
elif gp < 2.7 and gp >= 2.3:
    print(f'The equivalent letter grade for the grade point {gp} is C+')
elif gp < 2.0 and gp >= 2.0:
    print(f'The equivalent letter grade for the grade point {gp} is C')
elif gp < 1.7 and gp >= 1.7:
    print(f'The equivalent letter grade for the grade point {gp} is C-')
elif gp < 1.3 and gp >= 1.3:
    print(f'The equivalent letter grade for the grade point {gp} is D+')
elif gp < 1.3 and gp >= 1.0:
    print(f'The equivalent letter grade for the grade point {gp} is D')
elif gp < 1.0 and gp >= 0:
    print(f'The equivalent letter grade for the grade point {gp} is F')
else:
    print(f'The equivalent letter grade for the grade point {gp} is not known')

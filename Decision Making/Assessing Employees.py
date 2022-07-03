r = float(input('Enter the rating of the employee: '))
if r == 0.0:
    print(
        f'The employee with rating of {r} is having an Unacceptable Performance, so no salary hike is possible')
elif r == 0.4:
    s1 = r * 2400.00
    print(
        f'The employee with rating of {r} is having an Acceptable Performance, so the salary hike is possible and the amount of hike he/she will get upon his/her previous salary is {s1}')
elif r >= 0.6:
    s2 = r * 2400.00
    print(
        f'The employee with rating of {r} is having an Meritorious Performance, so the salary hike is possible and the amount of hike he/she will get upon his/her previous salary is {s2}')

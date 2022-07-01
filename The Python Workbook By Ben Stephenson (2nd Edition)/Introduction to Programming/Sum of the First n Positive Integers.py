n = int(input('Enter a positive integer of your choice: '))
if n % 2 == 0:
    sum = int(((n) * ((n) + 1)) / 2)
    print(f'Sum of the first {n} positive integers is: {sum}')
else:
    print(f'Your entered number is {n} which is not an even number')

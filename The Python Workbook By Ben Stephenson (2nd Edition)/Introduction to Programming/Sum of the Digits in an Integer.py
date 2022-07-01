n = int(input('Enter a 4 digit number: '))
strr = str(n)
if len(strr) == 4:
    tot = 0
    while (n > 0):
        dig = n % 10
        tot = tot + dig
        n = n // 10
    print(f'The total sum of digits is: {tot}')
else:
    print(f'Your entered number is {n} which is not a 4 digit number')

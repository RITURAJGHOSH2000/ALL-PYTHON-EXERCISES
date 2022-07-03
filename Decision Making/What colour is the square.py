pos = input('Enter the position in between a1 and h8 (like d6): ')
l = pos[0]
n = int(pos[1])
while l < 'i' and n < 9:
    if l == 'a' or l == 'c' or l == 'e' or l == 'g':
        if n == 1 or n == 3 or n == 5 or n == 7:
            print('The square is black in colour')
        elif n == 2 or n == 4 or n == 6 or n == 8:
            print('The square is white in colour')
    elif l == 'b' or l == 'd' or l == 'f' or l == 'h':
        if n == 1 or n == 3 or n == 5 or n == 7:
            print('The square is white in colour')
        elif n == 2 or n == 4 or n == 6 or n == 8:
            print('The square is black in colour')
    break
else:
    print(
        f'Your entered position value is {pos} which is not in between a1 and h8')

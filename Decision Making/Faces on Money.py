print('\nThe following table consists of the names of the individuals that appears on banknotes in the United States:-\n')
print('\t\t-----------------------------------------')
print('\t\t   Individual                   Amount')
print('\t\t-----------------------------------------')
print('\t\tGeorge Washington                 $1')
print('\t\tThomas Jefferson                  $2')
print('\t\tAbraham Lincoln                   $5')
print('\t\tAlexander Hamilton               $10')
print('\t\tAndrew Jackson                   $20')
print('\t\tUlysses S. Grant                 $50')
print('\t\tBenjamin Franklin               $100')
d = int(input('\nEnter the denomiantion of a banknote from the above list: $'))
if d == 1:
    print('The name of the individual present in the $1 banknote is George Washington')
elif d == 2:
    print('The name of the individual present in the $2 banknote is Thomas Jefferson')
elif d == 5:
    print('The name of the individual present in the $5 banknote is Abraham Lincoln')
elif d == 10:
    print('The name of the individual present in the $10 banknote is Alexander Hamilton')
elif d == 20:
    print('The name of the individual present in the $20 banknote is Andrew Jackson')
elif d == 50:
    print('The name of the individual present in the $50 banknote is Ulysses S. Grant')
elif d == 100:
    print('The name of the individual present in the $100 banknote is Benjamin Franklin')
else:
    print(f'The entered amount is ${d} which is not in the list')

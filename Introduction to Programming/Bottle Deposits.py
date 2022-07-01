number_of_small_bottles = int(input('Enter the number of drink containers holding one litre or less: '))
number_of_large_bottles = int(input('Enter the number of drink containers holding more than one litre: '))
refund1 = number_of_small_bottles * 0.10
refund2 = number_of_large_bottles * 0.254
refund3 = refund1 + refund2
refund = '{:.2f}'.format(refund3) 
print(f'The amount of refund you got for returing drink containers holding one litre or less is ${refund1}\nThe amount of refund you got for returing drink containers holding more than one litre is ${refund2}\nYour total refund is ${refund}')
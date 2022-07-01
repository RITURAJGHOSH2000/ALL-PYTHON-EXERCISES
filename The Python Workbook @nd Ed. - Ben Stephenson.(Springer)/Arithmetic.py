from cmath import log10
import math
a = int(input('Enter the first integer: '))
b = int(input('Enter the second integer: '))
print(f'Sum of {a} and {b} is: ', a + b)
print(f'Difference of {a} and {b} when {b} is subtracted from {a} is: ', b - a)
print(f'Product of {a} and {b} is: ', a * b)
print(f'Quotient when {a} is divided bt {b} is: ', a / b)
print(f'Remainder when {a} is divided by {b} is: ', a % b)
print(f'Result of log10({a}) is: ', log10(a))
print(f'The result of {a} to the power {b} is: ', a ** b)

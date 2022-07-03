import math
a = int(input('Enter the value of a: '))
if a == 0:
    print('Root(s) value will be infinite please enter atleast 1 or -1')
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))
d = (b ** 2) - (4 * a * c)
if d < 0:
    print(
        f'The quadratic equation f(x) = {a}x^2 + {b}x + {c} does not have any real roots')
elif d == 0:
    r = (-b) / (2 * a)
    print(
        f'The quadratic equation f(x) = {a}x^2 + {b}x + {c} has one real root which is {r}')
elif d > 0:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    r1_format = "{:.2f}".format(r1)
    r2_format = "{:.2f}".format(r2)
    print(
        f'The quadratic equation f(x) = {a}x^2 + {b}x + {c} have two real roots, which are {r1_format} and {r2_format}')

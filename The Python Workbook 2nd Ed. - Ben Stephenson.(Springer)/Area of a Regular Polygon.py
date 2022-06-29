from math import tan, pi
s = float(input('Enter the length of the sides of the regular polygon: '))
n = float(input('Enter the number of sides of the polygon: '))
area = (n * (s ** 2)) / (4 * tan(pi / n))
area_format = "{:.2f}".format(area)
print(
    f'Area of the polygon having {n} number of sides and side length of {s} is {area_format}')

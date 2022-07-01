from math import pi
r = float(input('Enter the radius of the cylinder, r = '))
h = float(input('Enter the height of the cylinder, h = '))
volume = pi * (r ** 2) * h
volume_format = "{:.1f}".format(volume)
print(f'Volume of the cylinder is {volume_format}')

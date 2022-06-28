from math import pi
radius = float(input('Enter the radius, r = '))
area = pi * (radius ** 2)
volume = (4 / 3) * pi * (radius ** 3)
area_format = "{:.3f}".format(area)
volume_format = "{:.3f}".format(volume)
print(
    f'Area of the circle of radius {radius} is {area_format}\nThe volume of the sphere with radius {radius} is {volume_format}')

b = float(input('Enter the base length of the triangle, b = '))
h = float(input('Enter the height of the triangle, h = '))
area = (b * h) / 2
area_format = "{:.1f}".format(area)
print(
    f'The area of the triangle with base length of {b} and height of {h} is {area_format}')

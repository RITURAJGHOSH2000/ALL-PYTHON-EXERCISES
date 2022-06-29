from math import sqrt
s1 = float(input('Enter the length of 1st side of the triangle: '))
s2 = float(input('Enter the length of 2nd side of the triangle: '))
s3 = float(input('Enter the legth of 3rd side of the triangle: '))
s = (s1 + s2 + s3) / 2
area = sqrt(s * (s - s1) * (s - s2) * (s - s3))
area_format = "{:.2f}".format(area)
print(
    f'The area of the triangle with side lengths as {s1}, {s2} and {s3} is {area_format}')

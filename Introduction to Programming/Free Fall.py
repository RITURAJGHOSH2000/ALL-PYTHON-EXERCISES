from math import sqrt
h = float(input('Enter the height from which the object is dropped (in m): '))
vf = sqrt((0 ** 2) + 2 * (9.8 * h))
print(
    f'The speed at which the object will travel after hitting the ground is {vf} m/s')

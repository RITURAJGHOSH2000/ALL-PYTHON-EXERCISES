import math
t1 = float(input('Enter the latitude value of first point (in degrees): '))
g1 = float(input('Enter the longitude value of first point (in degrees): '))
t2 = float(input('Enter the latitude value of second point (in degrees): '))
g2 = float(input('Enter the longitude value of second point (in degrees): '))
T1 = math.radians(t1)
G1 = math.radians(g1)
T2 = math.radians(t2)
G2 = math.radians(g2)
dlong = G2 - G1
dlati = T2 - T1
a = math.sin(dlati / 2)**2 + math.cos(T1) * \
    math.cos(T2) * math.sin(dlong / 2)**2
c = 2 * math.asin(math.sqrt(a))
radius = 6371.01
print(
    f'The distance between the two points ({t1}, {g1}) and ({t2}, {g2}) is: ', c * radius, ' KM')

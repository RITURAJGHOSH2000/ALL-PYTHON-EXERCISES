m = float(input('Enter the mass of water (in g): '))
dt = float(input('Enter the temperature change (in °C): '))
q = m * 4.186 * dt
q_format = "{:.3f}".format(q)
print(
    f'The total amount of energy that must be added or removed to achieve the desired temperature change is {q_format} J')
kwh = q * 0.0000002778
cost = kwh * 8.9
cost_format = "{:.2f}".format(cost)
print(
    f'The cost of boiling the water needed for a cup of coffee is Rs{cost_format}')

C = float(input('Enter the temperature (in °C): '))
F = (C * (9 / 5)) + 32
K = C + 273.15
K_format = "{:.2f}".format(K)
print(
    f'The temperature of {C}°C when converted to Fahrenheit is {F}°F\nAnd when {C}°C converted to Kelvin is {K_format}°K')

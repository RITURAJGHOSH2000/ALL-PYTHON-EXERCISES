ft = float(input('Enter the measurement (in ft): '))
inches = ft * 12
yards = ft * 0.33333
miles = ft * 0.00018
inches_format = "{:.2f}".format(inches)
yards_format = "{:.2f}".format(yards)
miles_format = "{:.5f}".format(miles)
print(f'The measurement that you entered was {ft} ft and, \nThe corresponding measurment in inches is {inches_format} in\nThe corresponding measurment in yards is {yards_format} yd\nThe corresponding measurement in miles is {miles_format} mi')

ft = float(input('Enter your height (in ft): '))
cm = ft * 12 * 2.54
cm_format = "{:.2f}".format(cm)
print(f'Your height is {cm_format} cms')

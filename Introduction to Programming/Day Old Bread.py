number_of_day_old_bread = int(input('Enter the number of day old breads: '))
fresh_bread_price = 3.49
day_old_bread_price = number_of_day_old_bread * fresh_bread_price * 0.60
day_old_bread_price_format = "{:.2f}".format(day_old_bread_price)
price_to_pay = fresh_bread_price - day_old_bread_price
price_to_pay_format = "{:.2f}".format(price_to_pay)
print(f'The regular price of the fresh bread is ${fresh_bread_price}\nAs the bread is a day old so it has a discount of 60%\nThe price which will be deducted due to discounht is {day_old_bread_price_format}\nThe price you have to pay is ${price_to_pay_format}')

meal_cost = int(input('Enter the cost of the meal: Rs '))
meal_tax = meal_cost * 0.05
meal_tip = meal_cost * 0.18
total_meal_cost = meal_cost + meal_tax + meal_tip
print(f'The cost of your meal is Rs {meal_cost}\nTax on your meal is Rs {meal_tax}\nTip on your meal is Rs {meal_tip}\nTotal cost of your meal is Rs {total_meal_cost}')
print('\n---------------Welcome to your SBI Savings Account---------------')
amount = float(
    input('\nEnter the amount you want to deposit in your savings account: Rs '))
print(
    f'\nYou have successfully deposited Rs {amount} in your savings account. The rate of interest for your savings account is 4%\n\nThe estimated savings growth for your account are:\n')
year = 1
while year < 4:
    CI = (amount * (1 + (4 / 100)) ** year) - amount
    update_amount = amount + CI
    update_amount_format = float("{:.2f}".format(update_amount))
    print(f'\t\tAfter {year} year(s) is: Rs {update_amount_format}\n')
    year += 1
print('\n\t---X--- (: THANKS FOR USING SBI SAVINGS ACCOUNT :) ---X---\n')

nm = int(input('Enter the number of minutes of air time used in a month: '))
nt = int(input('Enter the number of text messages used in a month: '))
b = 15.00
if nm <= 50 and nt <= 50:
    am = 0
    at = 0
    f_911 = 0.44
    amt = b + am + at + f_911
    tax = amt * 0.05
    t_amt = amt + tax
    print(f'You have used {nm} number of minutes of air time and {nt} number of text messages in this month.\nFollowing is the charge break-up for this month:\nBase Charge: ${b}\nYour Additional Minutes are: {am} min(s)\nEquivalent Additional Minutes Charge: ${am}\nYour Additional Text Messages are: {at} message(s)\nEquivalent Additional Text Message Charge: ${at}\nThe 911 fee: ${f_911}\nSales Tax: ${tax}\nTotal Bill Amount: ${t_amt}')
elif nm > 50 and nt > 50:
    am = nm - 50
    at = nt - 50
    amc = am * 0.25
    amc_format = "{:.2f}".format(amc)
    atc = at * 0.15
    atc_format = "{:.2f}".format(atc)
    f_911 = 0.44
    amt = b + amc + atc + f_911
    tax = amt * 0.05
    tax_format = "{:.2f}".format(tax)
    t_amt = amt + tax
    t_amt_format = "{:.2f}".format(t_amt)
    print(f'You have used {nm} number of minutes of air time and {nt} number of text messages in this month.\nFollowing is the charge break-up for this month:\nBase Charge: ${b}\nYour Additional Minutes are: {am} min(s)\nEquivalent Additional Minutes Charge: ${amc_format}\nYour Additional Text Messages are: {at} message(s)\nEquivalent Additional Text Messages Charge: ${atc_format}\nThe 911 fee: ${f_911}\nSales Tax: ${tax_format}\nTotal Bill Amount: ${t_amt_format}')
elif nm <= 50 and nt > 50:
    am = 0
    at = nt - 50
    atc = at * 0.15
    atc_format = "{:.2f}".format(atc)
    f_911 = 0.44
    amt = b + am + atc + f_911
    tax = amt * 0.05
    tax_format = "{:.2f}".format(tax)
    t_amt = amt + tax
    t_amt_format = "{:.2f}".format(t_amt)
    print(f'You have used {nm} number of minutes of air time and {nt} number of text messages in this month.\nFollowing is the charge break-up for this month:\nBase Charge: ${b}\nYour Additional Minutes are: {am} min(s)\nEquivalent Additional Minutes Charge: ${am}\nYour Additional Text Messages are: {at} message(s)\nEquivalent Additional Text Messages Charge: ${atc_format}\nThe 911 fee: ${f_911}\nSales Tax: ${tax_format}\nTotal Bill Amount: ${t_amt_format}')
elif nm > 50 and nt <= 50:
    am = nm - 50
    at = 0
    amc = am * 0.25
    amc_format = "{:.2f}".format(amc)
    f_911 = 0.44
    amt = b + amc + at + f_911
    tax = amt * 0.05
    tax_format = "{:.2f}".format(tax)
    t_amt = amt + tax
    t_amt_format = "{:.2f}".format(t_amt)
    print(f'You have used {nm} number of minutes of air time and {nt} number of text messages in this month.\nFollowing is the charge break-up for this month:\nBase Charge: ${b}\nYour Additional Minutes are: {am} min(s)\nEquivalent Additional Minutes Charge: ${amc_format}\nYour Additional Text Messages are: {at} message(s)\nEquivalent Additional Text Messages Charge: ${at}\nThe 911 fee: ${f_911}\nSales Tax: ${tax_format}\nTotal Bill Amount: ${t_amt_format}')

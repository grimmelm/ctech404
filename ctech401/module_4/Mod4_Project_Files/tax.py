# Get the command line input
import sys
income = int(sys.argv[1])

# Work through the different tax brackets and store the tax required in x
if income >= 0 and income <= 9275:
    x = 0.1*income
elif income > 9275 and income <= 37650:
    x = 927.5 + 0.15*(income - 9275)
elif income > 37650 and income <= 91150:
    x = 5183.75 + 0.25*(income - 37650)
elif income > 91150 and income <= 190150:
    x = 18558.75 + 0.28*(income - 91150)
elif income > 190150 and income <= 413350:
    x = 46278.75 + 0.33*(income - 190150)
elif income > 413350 and income <= 415050:
    x = 119934.75 + 0.35*(income - 413350)
elif income > 415050:
    x = 120529.75 + 0.396*(income - 415050)

# Round as the IRS request (0.5 and above up to 1, anything less round down)
rounded = int(x)
if x >= (float(rounded)+0.5):
    taxDue = rounded+1
else:
    taxDue = rounded

print('Tax due: $' + str(taxDue))

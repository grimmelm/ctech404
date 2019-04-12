# Get income input
income = int(input('Enter your income: '))

# Work through the different tax brackets and store the tax required in x
if income >= 0 and income <= 9525:
    x = 0.1*income
elif income > 9525 and income <= 38700:
    x = 952.50 + 0.12*(income - 9525)
elif income > 38700 and income <= 82500:
    x = 4453.50 + 0.22*(income - 38700)    
elif income > 82500 and income <= 157500:
    x = 14089.50 + 0.24*(income - 82500)    
elif income > 157500 and income <= 200000:
    x = 32089.50 + 0.32*(income - 157500)
elif income > 200000 and income <= 500000:
    x = 45689.50 + 0.35*(income - 200000)
elif income > 500000:
    x = 150689.50 + 0.37*(income - 5000000)

# Round as the IRS request (0.5 and above up to 1, anything less round down)
rounded = int(x)
if x >= (float(rounded)+0.5):
    taxDue = rounded+1
else:
    taxDue = rounded

print('Tax due: $' + str(taxDue))
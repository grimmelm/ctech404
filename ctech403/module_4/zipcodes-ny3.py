import csv

zip_codes_in_ny = 0

with open('zipcodes.csv') as f:
    for row in csv.reader(f):
        if row[3] == 'NY':
            zip_codes_in_ny += 1

print('There are ' + str(zip_codes_in_ny) + ' zip codes in New York.')

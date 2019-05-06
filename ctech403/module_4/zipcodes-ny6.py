import csv

# Split CSV file into a list of lines
with open('zipcodesnamed.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    zip_codes_table = list(reader)

zip_codes_in_ny = 0
for row in zip_codes_table:
    if row[3] == 'NY':
        zip_codes_in_ny += 1

print('There are ' + str(zip_codes_in_ny) + ' zip codes in New York.')

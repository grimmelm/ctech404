# Split CSV file into a list of lines
f = open('zipcodes.csv')
lines = f.read().splitlines()
f.close()

# Split each line on the commas
zip_codes_table = []
for line in lines:
    fields = line.split(',')
    zip_codes_table.append(fields)

zip_codes_in_ny = 0
for row in zip_codes_table:
    if row[3] == 'NY':
        zip_codes_in_ny += 1

print('There are ' + str(zip_codes_in_ny) + ' zip codes in New York.')

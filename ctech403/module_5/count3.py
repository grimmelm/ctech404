import csv

def count_zipcodes (rows, state):
    count = 0
    for row in rows:
        if row['State'] == state:
            count += 1
    return count

# Split CSV file into a list of lines
with open('zipcodesnamed.csv') as f:
    reader = csv.DictReader(f)
    zip_codes_table = list(reader)

print('New York: '+ str(count_zipcodes(zip_codes_table, 'New York')))
print('New Jersey: '+ str(count_zipcodes(zip_codes_table, 'New Jersey')))
print('New Hampshire: '+ str(count_zipcodes(zip_codes_table, 'New Hampshire')))
import csv

def count_matches(rows, field, value):
    count = 0
    for row in rows:
        if row[field] == value:
            count += 1
    return count

# Split CSV file into a list of lines
with open('zipcodesnamed.csv') as f:
    reader = csv.DictReader(f)
    zip_codes_table = list(reader)

print('New York: '+ str(count_matches(zip_codes_table, 'State', 'New York')))
print('Atlanta: '+ str(count_matches(zip_codes_table, 'City', 'Albany')))
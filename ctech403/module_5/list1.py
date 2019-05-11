import csv

def list_matches(rows, field, value):
    matches = []
    for row in rows:
        if row[field] == value:
            matches.append(row['Zip Code'])
    return matches

# Split CSV file into a list of lines
with open('zipcodesnamed.csv') as f:
    reader = csv.DictReader(f)
    zipcodes = list(reader)

zipcodes_in_ny = list_matches(zipcodes, 'State', 'New York')
print(zipcodes_in_ny)
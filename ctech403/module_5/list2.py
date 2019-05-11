import csv

def where(rows, field, value):
    matches = []
    for row in rows:
        if row[field] == value:
            matches.append(row)
    return matches

def select(rows, field):
    values = []
    for row in rows:
        values.append(row[field])
    return values

# Split CSV file into a list of lines
with open('zipcodesnamed.csv') as f:
    reader = csv.DictReader(f)
    zipcodes = list(reader)

cities_in_ny = select(where(zipcodes, 'State', 'New York'), 'City')
print(cities_in_ny)
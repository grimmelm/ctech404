import csv

# Split CSV file into a list of lines
with open('zipcodesnamed.csv') as f_in:
    reader = csv.DictReader(f_in)
    zip_codes_table = list(reader)

# Write only zip codes north of 40 degrees
with open('zipcodesnamed-out.csv','w') as f_out:
    headers = zip_codes_table[0].keys()
    writer = csv.DictWriter(f_out, headers)
    writer.writeheader()
    for row in zip_codes_table:
        if float(row['Latitude']) > 40:
            writer.writerow(row)
import csv

# Split CSV file into a list of lines
with open('zipcodesnamed.csv') as f_in:
    reader = csv.reader(f_in)
    headers = next(reader)
    zip_codes_table = list(reader)

# Write only zip codes north of 40 degrees
with open('zipcodesnamed-out.csv','w') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(headers)
    for row in zip_codes_table:
        if float(row[5]) > 40:
            writer.writerow(row)
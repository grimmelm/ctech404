import csv

# Split CSV file into a list of lines
with open('zipcodes.csv') as f_in:
    reader = csv.reader(f_in)
    zip_codes_table = list(reader)

# Write only zip codes north of 40 degrees
with open('zipcodes_out.csv','w') as f_out:
    writer = csv.writer(f_out)
    for row in zip_codes_table:
        if float(row[5]) > 40:
            writer.writerow(row)

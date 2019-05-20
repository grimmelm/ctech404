from basicdb import *
with open('zipcodesnamed.csv') as f:
    reader = csv.DictReader(f)
    zipcodes = list(reader)

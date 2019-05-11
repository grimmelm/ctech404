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

def db_sum(rows, field):
    total = 0
    for row in rows:
        total = total + float(row[field])
    return total

with open('courses.csv') as f:
    reader = csv.DictReader(f)
    courses = list(reader)

with open('rooms.csv') as f:
    reader = csv.DictReader(f)
    rooms = list(reader)

def join(rows1, rows2, field):
    new_rows = []
    for row1 in rows1:
        for row2 in rows2:
            if row1[field] == row2[field]:
                new_row = {}
                new_row.update(row1)
                new_row.update(row2)
                new_rows.append(new_row)
    return new_rows


total_capacity = db_sum(join(where(courses, 'times', 'MW10'), rooms, 'roomid'), 'capacity')

print('The total capacity is ' + str(total_capacity))
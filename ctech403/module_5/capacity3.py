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

with open('courses.csv') as f:
    reader = csv.DictReader(f)
    courses = list(reader)

with open('rooms.csv') as f:
    reader = csv.DictReader(f)
    rooms = list(reader)

def join_pair(rows1, rows2, join_field, field1, field2):
    new_rows = []
    for row1 in rows1:
        for row2 in rows2:
            if row1[join_field] == row2[join_field]:
                new_rows.append({field1 : row1[field1], field2 : row2[field2]})
    return new_rows

for join_row in join_pair(courses, rooms, 'roomid', 'coursename', 'capacity'):
    print('The enrollment limit for ' + join_row['coursename'] + ' is ' + join_row['capacity'])
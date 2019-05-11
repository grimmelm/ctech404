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

for course_row in courses:
    for room_row in rooms:
        if room_row['roomid'] == course_row['roomid']:
            print('The enrollment limit for ' + course_row['coursename'] + ' is ' + room_row['capacity'])
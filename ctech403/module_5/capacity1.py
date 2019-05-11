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


course_row = where(courses, 'coursename', 'Organic Chemistry')[0]
room = course_row['roomid']
room_row = where(rooms, 'roomid', room)[0]
capacity = room_row['capacity']

print('The enrollment limit is ' + capacity)
import csv

def count_matches(rows, field, value):
    count = 0
    for row in rows:
        if row[field] == value:
            count += 1
    return count

# Split CSV file into a list of lines
with open('courses.csv') as f:
    reader = csv.DictReader(f)
    courses = list(reader)

print('Meets at MW10: '+ str(count_matches(courses, 'times', 'MW10')))
print('Room 1002: ' + str(count_matches(courses, 'roomid', '1002')))
print('3 credits: ' + str(count_matches(courses, 'credits', '3')))

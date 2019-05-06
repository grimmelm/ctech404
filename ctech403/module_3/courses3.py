import json

with open('courses.json') as f:
    all_courses = json.load(f)
    
names = []
for course in all_courses:
    names.append(course['name'])
names.sort()

print(names)
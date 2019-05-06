import json

with open('courses.json') as f:
    all_courses = json.load(f)
    
print('There are ' + str(len(all_courses)) + ' courses')
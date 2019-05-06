import json

with open('courses.json') as f_in:
    all_courses = json.load(f_in)
    
for course in all_courses:
    if course['course id'] >= 2000:
        course['credits'] += 1

with open('courses-out.json', 'w') as f_out:
    json.dump(all_courses, f_out)
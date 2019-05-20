import sqlite3

dbname = 'registrar.sqlite'

connection = sqlite3.connect(dbname)
c = connection.cursor()

c.execute('SELECT * FROM courses;')
rows = c.fetchall()
print("\nAll fields from all courses")
print(rows)


c.execute('SELECT coursename FROM courses WHERE times = \'MW10\';')
rows = c.fetchall()
print("\nCourse names meeting MW at 10")
print(rows)

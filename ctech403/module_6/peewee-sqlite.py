from peewee import *

db = SqliteDatabase('registrar-peewee.sqlite')

class BaseModel(Model):
    class Meta:
        database = db

class Students(BaseModel):
    lastname = TextField()
    firstname = TextField()
    studentid = IntegerField(primary_key=True)

class Courses(BaseModel):
    courseid = IntegerField(primary_key=True)
    coursename = TextField()
    roomid = IntegerField()
    times = TextField()
    credits = IntegerField()

class Rooms(BaseModel):
    roomid = IntegerField(primary_key=True)
    roomname = TextField()
    capacity = IntegerField()
    
class Enrollments(BaseModel):
    studentid = IntegerField()
    courseid = IntegerField()
    class Meta:
        primary_key = False

for i in Students.select():
    print (i.firstname + ' ' + i.lastname)
print()

for i in Rooms.select().where(Rooms.capacity > 20):
    print (i.roomname + ' has capacity ' + str(i.capacity))
print()

for i in Courses.select().join(Rooms, on = (Courses.roomid == Rooms.roomid)).where(Rooms.capacity > 20):
    print(i.coursename + ' meets in a room with capacity > 20')


count(where(zipcodes, 'State', 'New York'))

ks_latitudes = select(where(zipcodes, 'State', 'Kansas'),'Latitude')
mean_latitude = sum(ks_latitudes, 'Latitude') / count(ks_latitudes)

select(orderby(zipcodes,'Longitude'), 'Zip Code')

distinct(select(where(zipcodes, 'Locality', 'Springfield'), 'State'))


db_sum(join(where(courses, 'times', 'MW10'), rooms, 'roomid'), 'capacity')

db_sum(join(where(db_from('courses'), 'times', 'MW10'), db_from('rooms'), 'roomid'), 'capacity')


insert('rooms', {'roomid': 2003', 'roomname': 'Physics Lab', 'capacity' : 20})

insert('rooms', [{'roomid': 2003', 'roomname': 'Physics Lab', 'capacity' : 20}])

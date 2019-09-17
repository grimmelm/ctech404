office_numbers = {'Frank Pietro': 204, 'Jennifer Moth': 103, 'Barbara Wilson': 245, 'Mark Opengher' : 215, 'Ronald Davis': 335, 'Minnie Potter': 207, 'Joseph Smith': 130, 'Christopher Neals': 167, 'Georgia Thompson': 307}

for d in office_numbers:
	if office_numbers[d] < 300 and office_numbers[d] >=200:
		office_numbers[d] = office_numbers[d] + 100
	
print(office_numbers)


office_numbers = {'Frank Pietro': 204, 'Jennifer Moth': 103, 'Barbara Wilson': 245, 'Mark Opengher' : 215, 'Ronald Davis': 335, 'Minnie Potter': 207, 'Joseph Smith': 130, 'Christopher Neals': 167, 'Georgia Thompson': 307}
office_updates = {215: 370, 207: 304, 245: 325, 204: 399} 

for d in office_numbers:
	if office_numbers[d] < 300 and office_numbers[d] >=200:
		new_value = office_updates[office_numbers[d]]
		office_numbers[d] = new_value


print(office_numbers)

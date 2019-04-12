grade = int(input('Enter your grade:'))

if grade >= 90:
	print('You received an A!')
	if grade == 100:
		print('Perfect Score!')
elif grade >= 80:
	print('You received a B!')
elif grade >= 70:
	print('You received a C!')
elif grade >= 60:
	print('You received a D!')
else:
	print('You failed!')
	
	

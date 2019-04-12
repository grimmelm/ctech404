###Question #1
#
#  MC: <br>
#1. I have a truck too/Blue is the best  
#2. I have a truck too/I dont like blue 
#3. I have a truck too/I dont like red 
#4. No output
#
#

vehicle = input('Enter a vehicle: ')
color = input('Enter a color: ')

if vehicle == 'truck':
	print('I have a truck too.')
	if color == 'blue':
    	print('Blue is the best!')
  	else:
     	print('I don\'t like' + ' ' + color)


###Question #2
#MC
#1. I have a car too/I dont like red. 
#2. I dont have a car either
#3. I dont have a car either/I love silver/I love red
#4. I dont have a car either/I love red
#
	
vehicle = input('Enter a vehicle: ')
color = input('Enter a color: ')

if vehicle == 'car':
	print('I have a car too.')
	if color == 'blue':
		print('Blue is the best!')
    else:
    	print('I don\'t like' + ' ' + color)

else:
	print('I don\'t have a car either)
	if color == 'silver':
		print('I love silver!')
	if color == 'red':
		print('I love red!')	
	
###Question #3
#
#MC
#1. I have a car too/I dont like red. 
#2. I have a car too/Blue is the best
#3. I have a car too
#4. No output
#
	
vehicle = input('Enter a vehicle: ')
color = input('Enter a color: ')

if vehicle == 'car':
	print('I have a car too.')
	if color == 'blue':
		print('Blue is the best!')
    else:    
      print('I don\'t like' + ' ' + color)
      	
###Question #4
#
# MC
#1. I have a car too 
#2. I wish I had a bike!
#3. Awesome!
#4. No output
#	  
#OR T/F this produces no output?
#


vehicle = input('Enter a vehicle: ')
if vehicle == 'car':
	print('Cool. I have a car too!')
elif vehicle == 'van':
	print('Cool. I don\'t like vans much, sorry!')
elif vehicle == 'bike':
	print('Cool. I wish I had a bike!')
else:
	print('Awesome!')	
	
	
	
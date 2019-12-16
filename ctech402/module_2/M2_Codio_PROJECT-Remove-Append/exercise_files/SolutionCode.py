Part 1:
	
integer_list = [10,2,5,7,4,3,6,9,8,1]
list_even = []
list_odd = []

for i in integer_list:
	if i%2 == 0:
		list_even.append(i)
	else:
		list_odd.append(i)


print("Even numbers: " + str(sorted(list_even)))
print("Odd numbers: " + str(sorted(list_odd)))

Part 2:

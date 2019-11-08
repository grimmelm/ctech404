prime_numbers = [ 2, 10, 25, 11, 5, 3, 97, 93, 100]
remove = []

for i in prime_numbers:
	for n in range(2, i): # 2,3,4,5...up to the array value
		if i % n == 0:
			remove.append(i)
			#break

for r in remove:
	if r in prime_numbers:
		prime_numbers.remove(r)
------------------
# Remove all odd numbers:
	
numbers = [ 2, 10, 25, 11, 5, 3, 97, 93, 100]
items_to_remove = []

for i in numbers:
	if i % 2 == 1:
		items_to_remove.append(i)
			

for r in items_to_remove:
	numbers.remove(r)

print(numbers)

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

print(prime_numbers)

s = input('Enter a string:')

def return_vowel_count(vowel, string):
	
	vowels = ['a', 'e', 'i', 'o', 'u', 'y']
	count = 0
	for s in string:
		for v in vowels:
			if v in s.lower():
				count = count + 1
	return count
	
vowel_counts =  str(return_vowel_count('l', s))
print('there are ' + vowel_counts + ' vowels in ' + s)

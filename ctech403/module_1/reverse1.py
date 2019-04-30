# Read input.txt into the list
with open('input.txt') as f_in:
	lines = f_in.readlines()

# Write the list in reverse to output.txt
with open('output.txt', 'w') as f_out:
	for line in reversed(lines):
		print(line, file=f_out)

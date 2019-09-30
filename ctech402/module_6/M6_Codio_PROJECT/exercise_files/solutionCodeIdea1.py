####
# 
# Player and Computer each have 5 dice
# They each roll all 5 dice one time
# They are allowed to re-roll ONE die.
#
#######

import random

player_score = 0
computer_score = 0

# define roll function
def roll_one_die():

	v = random.randint(1,6)
	print("rolled: " + str(v))
	return v
	
	
def compute_total(list_of_values):

	total = 0
	for val in list_of_values:
		total = total + val
	
	return total

# Computer and user roll below:

print("computer: ")
comp_values = []
for i in range(5):
	comp_values.append(roll_one_die())
computer_score = compute_total(comp_values)
print("score: " + str(computer_score))

player_values = []
print("You: ")
for i in range(5):
	player_values.append(roll_one_die())
	
player_score = compute_total(player_values)
print("score: " + str(player_score))
 
# prompt user to re-roll one die below:

response =  input("would you like to re-roll one die? Y/N")
if response.upper() == 'Y':
	choice = int(input("which die would you like to re-roll [die 1...die 6]?"))
	if choice >=1 and choice <=6:
		player_values.remove(player_values[choice-1])
		player_values.append(roll_one_die())
		print(player_values)  # can do this better for formatting purposes...
		player_score = compute_total(player_values)
		print("Your score: " + str(player_score))
 
# print final score and report who wins below:

if computer_score > player_score:
	print("COMPUTER WINS :(" )
elif player_score > computer_score:
	print("YOU WIN!!! :) " )
else:
	print("TIED!")
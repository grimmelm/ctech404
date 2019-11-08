####
# 
# Player and Comp each have 5 dice
# They compete for X rounds:
# 	They each roll all 5 dice X times 
# User is allowed to re-roll all 5 dice once during each round
#
#######

import random

# total score
player_score = 0
computer_score = 0

# save the score for each round
player_hand = []
computer_hand  = []

# define roll function
def roll():

	total = 0
	for i in range(5):
		r = random.randint(1,6)
		print(str(r))
		total = total + r
	
	return total 
	
# prompt user for number of rounds

response =  int(input("how many times do you want to roll?"))

# Both computer and player roll below:

for i in range(response):
	print("role # " + str(i+1))
	
	print("computer: ")
	score = roll()
	print("score: " + str(score))
	computer_hand.append(score)

	print("You: ")	
	score = roll()
	print("score: " + str(score))
	

for i in player_hand:
	player_score = player_score + i
	
for i in computer_hand:
	computer_score =computer_score + i


# Final score reported to user: 

print("Computer scored: " + str(computer_score))
print("You scored: " + str(player_score))

if computer_score > player_score:
	print("COMPUTER WINS :(" )
elif player_score > computer_score:
	print("YOU WIN!!! :) " )
else:
	print("TIED!")
import random

# Set up the hands
player_hand = [1, 2, 3, 4, 5]
computer_hand = [1, 2, 3, 4, 5]

player_score = 0
computer_score = 0

# Repeat until there are no cards left:
while player_hand != []:
    # The player picks a card
    player_play = int(input('Pick a card: '))
    # The computer picks a card
    computer_play = random.choice(computer_hand)
    # The cards are removed from players' hands
    player_hand.remove(player_play)
    computer_hand.remove(computer_play)
    # Higher card wins a point
    if player_play > computer_play:
        player_score = player_score + 1
    elif player_play < computer_play:
        computer_score = computer_score + 1

# Show the final score
print('Final score:')
print('Player: ' + str(player_score))
print('Computer: ' + str(computer_score))

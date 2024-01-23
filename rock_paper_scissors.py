'''
4. Rock Paper scissors
'''

import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie' 
    if is_win(user, computer):
        return 'You won'
    return 'You loose'
    

# r > s, p > r, s > p
def is_win(player, opponent):
    # return if player win 
    if player == 'r' and opponent == 's' or player == 'p' and opponent == 'r' \
    or player == 's' and opponent == 'p':
        return True

print(play())

import random
r = 'rock'
p = 'paper'
s = 'scissors'

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("You both chose " + user + ". It's a tie!")

    # r > s, s > p, p > r
    elif win(user, computer):
        print("You chose " + user + " and the computer chose " + computer + ". You win!")

    elif loss(user, computer):
        print("You chose " + user + " and the computer chose " + computer + ". You lose!")

def win(user, computer):
    # return true if player wins
    # r > s, s > p, p > r
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True

def loss(user, computer):
    # return true if player wins
    # r > s, s > p, p > r
    if (user == 'r' and computer == 'p') or (user == 's' and computer == 'r') or (user == 'p' and computer == 's'):
        return True

print(play())
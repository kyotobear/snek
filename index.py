
import random

def game():
    user = input(" r, p, or s?: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It is a tie! :v"

    if winner(user, computer):
        return "You won :D!!"

    return "You lost :("


def winner(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True


print(game())
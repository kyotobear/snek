# r,p,s

import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        "it is a tie"


def winning(player, computer):
    if (player == "r" and computer == "s") or (player == "s" and computer == "p") or (player == "p" and computer == "r"):
        "player beats computer with: " + player + " and computer: " + computer
        
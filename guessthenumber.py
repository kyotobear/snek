"""
guess the number and see how well you guess it before 
you run out of turns!

use while loop to keep on going till condition is no longer met
while loop for each try

"""

import random

generator = random.randint(0, 100)
print(generator)

guess = 0
while True:
    user_choice = int(input("I am thinking of a number between 0 to 100: "))
    if user_choice < generator:
        guess += 1
        print("the number is slightly lower, guess again!" " guess count: " + str(guess))
    elif user_choice > generator:
        guess += 1
        print("the number is slightly higher, guess again!" + " guess count: " + str(guess))
    else:
        break

if user_choice == generator:
    guess += 1
    if guess == 1:
        print("You guessed my number within the " + str(guess) + "st attempt! WEEW")
    else:
        print("You guessed my number after " + str(guess) + " attempts! :D")
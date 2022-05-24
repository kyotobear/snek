import random

from words import words

# print(words)

word_choice = random.choice(words)

def split(word):
    return [char for char in word] * "*"


# show censored word
# if a user gets a character right, reveal the character within 
# censored word
# otherwise, keep user guessing till length of the word

newword = split(word_choice)
print(split(word_choice))


censoredword = len(word_choice) * "*"
# print(censoredword)

user = input("guess one letter in the word: ")

i = 0
cword = []
while i < len(word_choice):
    if user in newword:
        i+= 1 
        print(user)
    else:
        i+= 1
        cword += "*"
        print(cword)
        # print(censoredword)

# for char in word_choice:
#     if user in newword:
#         print(user)


# def guessWord():
#     user = input("guess one letter in the word: ")
#     censoredword = len(word_choice) * "*"
    
#     for char in 
#     split(word_choice)
#     if user == 

# print(guessWord())

import random

from words import words

word_choice = random.choice(words)
print(word_choice)

def split(word):
    return [char for char in word]

word_split = split(word_choice)


# user_input = input("please guess a letter: ")


# print(word_choice.count(user_input))

# position = []
# for char in range(len(word_split)):
#     if word_split[char] == user_input:
#         position.append(char)
#         print(position)
#     else: 
#         pass


word_censored = len(word_choice) * "*"
print(word_choice.replace(word_choice, word_censored)
print(word_choice.replace())




# guess = input("guess a letter")

# for char in word_choice:




# word_choice = random.choice(words)

# def split(word):
#     return [char for char in word] 


# # show censored word
# # if a user gets a character right, reveal the character within 
# # censored word
# # otherwise, keep user guessing till length of the word

# newword = split(word_choice)
# print(split(word_choice))


# censoredword = len(word_choice) * "*"
# # print(censoredword)

# user = input("guess one letter in the word: ")

# i = 0
# cword = []
# while i < len(word_choice):
#     if user in newword:
#         i+= 1 
#         print(user)
#     else:
#         i+= 1
#         cword += "*"
#         print(cword)
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

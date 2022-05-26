# Python Basic Exercises - Part 1 
# https://www.w3resource.com/python-exercises/python-basic-exercises.php

"""1. Write a 
Python program to 
print the following string in a 
specific format """

# def twinklestar(phrase):
# #     phrase.count("Twinkle, twinkle, little star,
# # ")

# second_statement = "How I wonder what you are! "
# first_statement = "Twinkle, twinkle, little star,"
# third_statement = "Up above the world so high,"
# fourth_statement = "Like a diamond in the sky."
# final_statement = "How I wonder what you are"
# final_statement = first_statement + "\n\t " + second_statement + "\n\t\t" + third_statement + "\n\t\t" + fourth_statement + "\n" + first_statement + "\n\t" + final_statement
# print(final_statement)
# print()

"""2. Write a Python program to get the Python version you are using. Go to the editor
"""
# python --version

"""Write a Python program to display the first and last colors from the following list"""
# color_list = ["Red", "Green", "White", "Black"]
# color1 = color_list[0]
# color2 = color_list[(len(color_list) - 1)]
# print(color1,color2)

"""69. Write a Python program to sort three integers without using conditional statements and loops."""


x = int(input("1st #: "))
y = int(input("2nd #: "))
z = int(input("3rd #: "))

a1 = min(x,y,z)
a3 = max(x,y,z)
a2 = (x + y + z) - a1 - a3
print("Numbers sorted in order: ", a1, a2, a3)
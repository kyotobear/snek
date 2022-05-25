# In this exercise, you must implement the rep_cat function. 
# You are given two integers, x and y, as arguments. You must convert them into strings.
#  The string value of x must be repeated 10 times and the string value of y must be repeated 5 times.

# At the end, y will be concatenated to x and the resulting string must returned.


# Sample Input#
# x = 3
# y = 4
# Sample Output#
# '333333333344444'


# def rep_cat(x, y):
#     string_x = str(x)
#     string_y = str(y)
#     concatenated = (string_x * 10) + (string_y * 5)
#     return concatenated

# print(rep_cat(3,4))

# In this challenge, you must implement the factorial() function.
#  It takes an integer as a parameter and calculates its factorial.
# #  Python does have a built-in factorial function but you’ll be creating your own for practice.
# The factorial of a number, n, is its product with all the integers between 0 and n.

# factorial for 0 and 1 is always 1.
# sample input n = 5
# sample output 120

# factorial(n) = n * (n-1) * (n-2) * 

# def factorial(n):
#     if n < 0:
#         return -1
#     elif n <= 1:
#         return n
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))


# def grid_paths(n,m):
#     if n == 1 or m == 1:
#         return 1 
#     else:
#         return grid_paths(n, m - 1) + grid_paths(n - 1, m)

# write a function that counts
# the number of ways you can partition/divide n objects
# using parts up to m (assuming m >= 0)

# def count_partitions(n,m):
#     if n == 0:
#         return 1
#     elif m == 0 or n < 0:
#         return 0
#     else:
#         return count_partitions(n-m, m) + count_partitions(n, m-1)


# Exercise: Balanced Brackets
"""Given a string containing only square brackets,
 [], you must check whether the brackets are balanced or not. The brackets are said to be balanced if, 
 for every opening bracket, there is a closing bracket.

You will write your code in the check_balance() function, 
which returns True if the brackets are balanced and False
 if they are not.

 For an empty string, the function will return True.
"""

def check_balance(brackets):  # The argument is a string
    pass  # Replace with your code



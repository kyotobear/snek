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
# def check_balance(brackets): 
#     if len(brackets) == 0:
#         return True
#     else:
#         for bracket in range(len(brackets)):
#             inside = brackets.count("]")
#             outside = brackets.count("[")
#             if inside == outside:
#                 return True
#             elif (inside > outside) or (outside > inside):
#                 return False
#             elif "][":
#                 return False

# print(check_balance("[[][]]"))


"""You must implement the check_sum() function 
which takes in a list and returns True if the sum of two numbers in the list is zero. 
If no such pair exists, return False.
sample input: [10, -14, 26, 5, -3, 13, -5]
sample output: True
"""

# def check_sum(num_list):
#     for n1 in num_list:
#         for n2 in num_list:
#             if(n1 + n2 == 0):
#                 return True
#     return False

# def check_sum(num_list):
#     for first_num in range(len(num_list)):
#         for second_num in range(first_num + 1, len(num_list)):
#             if num_list[first_num] + num_list[second_num] == 0:
#                 return True
#     return False


# num_list = [10, -14, 26, 5, -3, 13, -5]
# print(check_sum(num_list))



"""As we saw earlier, 
the Fibonacci sequence is a series of numbers 
where every number is the sum of the two numbers before it. The first two numbers are 
0 and 1:

0 1 1 2 3 5 8 13

Input: n = 7
Output: 8

If n is negative or zero, return -1.
"""

# list = []
# def fib(n):
#     num1 = 0
#     list.append(num1)
#     num2 = 1
#     i = 1
#     while i <= n:
#         sum = num1 + num2
#         num1 = num2
#         num2 = sum
#         list.append(num1)
#         i+=1
#     return list[n - 1]
    

# print(fib(7))


# outside solution
# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#             print(c)


"""Challenge 1: Square Numbers and Return Their Sum

Implement a class Point that has three properties 
and a method. All these attributes (properties and methods) 
should be public. 
This problem can be broken down into 
two tasks:
"""

# class Point:

#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z

    
#     def sqSum(self):
#         return (self.x **2 ) + (self.y ** 2) + (self.z ** 2)


# obj1  = Point(1,3,5)  

# print(obj1.sqSum())


"""
Implement a class - Student - 
that has four properties and two methods. All these attributes (properties and methods) should be public. This problem 
can be broken down into three tasks.

Implement a constructor to initialize the values of four properties: 
name, phy, chem, and bio.

Implement a method  totalObtained 
 in the Student class that 
 calculates total marks of a student.


Using the totalObtained method, implement another method, percentage, in the Student class that calculates the percentage of students marks. Assume that the total marks of each subject are 100. The combined marks of three subjects are 300.

The formula for calculating the percentage is given below.

Percentage=
Percentage=

TotalMarks
MarksObtained

"""

class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return (self.phy + self.chem + self.bio)

    def percentage(self):
        return((self.totalObtained()/300) * 100)
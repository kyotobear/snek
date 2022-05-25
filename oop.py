

# classes are defined as:
class ClassName:
    pass


# class naming rules:
# Must start with a letter or underscore
# Should only be comprised of numbers, letters. or underscores

# We can create an object of a class by simply using
# the name of the class followed by a pair of parenthesis

class myClass:
    pass

obj = myClass()
print(obj)


# 
# class Employee:
#     ID = None
#     salary = None
#     department = None 

"""# To access properties of an object, dot notation is used.
# object.property
"""


class Employee:
    ID = 3789
    salary = 200000
    department = "Engineering"

"""# creating an object of the Employee class"""
Kist = Employee()

# Assigning values to properties of Kist - an object of the Employee class
Kist.ID = 3789
Kist.salary = 2500
Kist.department = "Engineering"
# creating a new attribute for Kist
Kist.title = "Senior Engineer"
"""Printing the properties of Kist"""

print("Id = ", Kist.ID)
print("Salary", Kist.salary)
print("Department: ", Kist.department)
print("Title: ", Kist.title)
"""Creating properties outside a class"""
"""Note: The property, 
title, will only be added to Kist and all other future objects will only have the properties which are declared in the class."""


"""What is an initializer?
As the name suggests, the initializer is used to initialize an object of a class. 
Its a special method that outlines the steps that are 
performed when an object of a class is created in the program. It’s used to define and assign values to instance variables. We will discuss the concept of instance variables in the next lesson. 
For now, just focus on the syntax.

The intialization method is similar to other
methods but has a pre-defined name:
__init__
"""  

"""Initializers are called when an object of
a class is created."""
class Employee:
    # defining the properties and assigning them None
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = Employee(3789, 2500, "Human Resources")

# Printing properties of Steve
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)


"""Below is an example where one Employee class 
object is created without the initializer parameters 
and one is created with the initializer parameters.
"""

class Employee:
    # defining the properties and assigning None to them
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = Employee()
Mark = Employee("3789", 2500, "Human Resources")

# Printing properties of Steve and Mark
print("Steve")
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)
print("Mark")
print("ID :", Mark.ID)
print("Salary :", Mark.salary)
print("Department :", Mark.department)


"""In Python,
properties can be defined into two parts:
- Class variables
- Instance variables

class variables are shared by all instances or objects of the classes.
A change in the class variable will: 
change the value of the property in 
in all the objects of the class.

Instance variables: are unique to each instance
or object of the class.
A change in the instance variable will change the value of the property
in that specific object only.

Class variables are defined "OUTSIDE" of the initializer
while Instance variables are defined "INSIDE" the initializer.
"""

class Player:
    teamName = "Liverpool" #class variables

    def __init___(self, name):
        self.name = name #creating instance variables

p1 = Player("Mark")
p2 = Player("Kist")


print("Name:", p1.name)
print("Team Name:", p1.teamName)
print("Name:", p2.name)
print("Team Name:", p2.teamName)

 

#  Using class variables and instance variables
# properly

class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerTeams = []


p1 = Player('Mark')
p1.formerTeams.append('Barcelona')
p2 = Player('Steve')
p2.formerTeams.append('Chelsea')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams)


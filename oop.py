

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

"""
Interaction between properties
and other objects is where methods come into play.

three types of methods in Python:
1. instance methods
2. class methods
3. static methods

Will be discussing instance methods
in this lesson because they are the most used 
in Python OOP

The first parameter of the method 
should alwasy be self and which followed by the remaining
parameters
"""

# Example of implementing methods in a class

class Employee:
    # Defining the initializer
    def __init__(self, ID=None, salary =None, department = None):
        self.ID = ID
        self.salary = salary
        self.department = department
    
    def tax(self):
        return (self.salary * .2)

    def salaryPerDay(self):
        return (self.salary/30)

# Initializing an object of the Employee class
Steve = Employee(3789, 2500, "HR")

# Printing the properties of Steve
print("ID = ", Steve.ID)
print("Salary: ", Steve.salary)
print("Department: ", Steve.department)
print("Tax paid by Steve: ", Steve.tax())
print("Salary per day of Steve", Steve.salaryPerDay())


"""
To declare a method as a class method,
we use the decorator 
@classmethod. cls isued to refer to the class
just like self is used for object of the class.
"""

class MyClass:
    classVariable = "educative"

    @classmethod
    def demo(cls):
        return cls.classVariable


class Player:
    teamName = "Liverpool"

    def __init__(self, name):
        self.name = name
    
    @classmethod
    def getTeamName(cls):
        return cls.teamName

print(Player.getTeamName())

"""Static methods are methods that 
are usually limited to class only and not their
objects. They have no direct relation to class
variables or instance variables.
They are used as utility functions inside the class
or when we do not want the inherited classes. """


"""To declare a method as a static method,
we use the decorator @staticmethod.
It does not use a reference to the object or class,
so we do not have to use self or cls.
We can pass as many arguments as we want and use this
method to perform any function without interfering with the
instance or class variables."""

class MyClass:

    @staticmethod
    def demo()
    print("I am a static method")

p1 = Player("lol")
p1.demo()
Player.demo()



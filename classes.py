

from turtle import color


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight    

# when function is a method of a class - add additional argumnent self 
# add self to every method in the class
    def introduce_self(self):
        return print("My name is " + self.name + " and I am " + self.color + " and I weigh "  + str(self.weight) + " pounds")


obj1 = Robot("Nellie", "pink", 10)
obj2 = Robot("Tommie", "silver", 12)

print(obj1.introduce_self())
print(obj2.introduce_self())
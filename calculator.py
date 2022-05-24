
# def add(n1, n2):
#     return n1 + n2

# def sub(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1/n2


# def calculator(operation, n1, n2):
#     return operation(n1,n2)


# result = calculator(add, 1, 2)
# print(result)


# lambda is good for passing functions as arguments
# argument - value provided or passed into a function or method

def calculator(operation, n1, n2):
    return operation(n1, n2) #using 'operation' argument as a function

result = calculator(lambda n1, n2: n1 * n2, 10, 20)
print(result)
print(calculator(lambda n1, n2: n1 + n2, 5, 10))


# map function creates a map object using an existing list and a function as its parameters
# map(function, list)
# below - use map() to double the values of an existing list

num_list = [0,1,2,3,4,5]
double_list = map(lambda n: n * 2, num_list)
print(list(double_list))
# this creates a new list, the original list remains unchanged.


# filter() filters elements from a list if the elements satisfy the condition that is specified in the argument function.

numList = [30, 2, -15, 17, 9, 100]

greater_than_10 = list(filter(lambda n: n> 10, numList))
print(greater_than_10)

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
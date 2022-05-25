# def rec_count(number):
#     print(number)
#     #base case
#     if number == 0:
#         return 0
#     rec_count(number - 1) # A recursive call with a different argument
#     print(number)


# rec_count(5)
# Fibonacci sequence
# 0 1 1 2 3 5 8 13


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
 
nterms = 7

# check if the number of terms is valid
if nterms <=0:
    print("please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(fibonacci(i))





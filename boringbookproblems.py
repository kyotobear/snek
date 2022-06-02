import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    random_list = []
    for i in range(1, 101):
        randomNumber = random.randint(0, 1)
        random_list.append(randomNumber)
print(random_list)

count_one = 0
count_zero = 0

for n in random_list:
    if n == 1:
        count_one +=1 
        count_zero = 0
    elif n == 0:
        count_zero += 1
        count_one = 0

    if count_zero == 6 or count_one == 6:
        count_one = 0
        count_zero = 0
        numberOfStreaks += 1
        break 
print("Chance of Streak: " + str(numberOfStreaks/ 100))


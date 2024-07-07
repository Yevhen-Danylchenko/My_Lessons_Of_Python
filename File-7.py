import random

list = []

userInput = int(input('Задайте довжину списку: \t'))

for index in range(userInput) :

    list.append(random.randint(0, 500))

print(list)
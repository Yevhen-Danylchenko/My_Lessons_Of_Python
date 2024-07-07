import random

rundNum = random.randint(0, 101)

step = 0

while True :
    userNum = int(input("Задайте число: \t"))
    step += 1
    if userNum < rundNum :
        print("Ваше число меньше.\n")
    elif userNum > rundNum :
        print("Ваше число більше.\n")
    elif userNum < 0 or userNum >=100 :
        print("Неправильно задане число! \n")
    elif userNum == rundNum:
        print("Ви вгадали!")
        print(step)
        break
userInput = int(input("Задайте перше число.\t"))
userInputOne = int(input("Задайте друге число.\t"))

while userInput <= userInputOne :
        if userInput % 2 == 0 :
            print(userInput)
            break
        userInput += 1


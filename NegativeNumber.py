sum = 0

while True :
    userInput = int(input("Задайте число: \t"))
    if userInput < 0 :
        break
    sum += userInput
    print(sum)
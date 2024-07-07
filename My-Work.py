list = [1,4,'hello',5,-1,0,3.5]

userInput = ' '

while userInput.lower() != 'stop' :

    userInput = input('Введіть елемент у список: \t')

    list.append(userInput)

print(list)

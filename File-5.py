colors = ["red", "green","blue"]

userInput = str(input('Задайте новий колір: \t'))

for index, elem in enumerate(colors) :
    if elem == 'blue' :
        colors[index] = userInput

print(colors)
list = [1,4,'hello',5,-1,0,3.5]

userInput = ' '

for a in list :
    userInput = str(input('Задайте назву елементу: \t'))
    for index, elem in enumerate(list) :
        if str(elem) == userInput:
            list1 = list.remove(elem),list.copy()
            print(f'Елемент: {elem} видалено \n')
            print(list1)
            if str(elem) != userInput :
                print(f'Елемента {userInput} немає в списку. \n')






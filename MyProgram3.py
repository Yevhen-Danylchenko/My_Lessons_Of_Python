my_list = ["hello1" , "hello" , "hello3",-3,60,0]

userInput = input('Введіть данні: \t')

for index, elem in enumerate(my_list) :
    if userInput == str(elem) :

        print(index)


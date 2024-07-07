userInput = str(input('Введіть символ:\t'))

stringProgram = 's;oedfjhtg;oearihg;asoerigha;eorigha;oehrga;eorgha;'

num = 0

for index in stringProgram :
    if index == userInput :
        num += 1
print(num)

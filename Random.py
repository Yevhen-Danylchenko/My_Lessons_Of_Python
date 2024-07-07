import random
import string

userInput = int(input('Задайте довжину пароля: \t'))

passvord = str('')

strok = string.ascii_letters + string.digits + string.punctuation

for index in range(userInput) :
    passvord += random.choice(strok)
print(passvord)

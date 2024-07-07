import random

list = [1,0,3,5,0,5,50,0,2,4,0]

for index in range(len(list)) :
    if list[index] == 0 :
        list[index] = (random.randint(0, 200))

print(list)

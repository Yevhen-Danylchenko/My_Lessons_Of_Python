import random

sum = 0
sum1 = 0

for a in range(100) :

    rund = random.randint(0, 1)
    if rund == 1 :
        sum += 1

    elif rund == 0 :
        sum1 += 1

if sum > sum1 :
    print("Виграв Орел! \n")
    print(sum)

elif sum < sum1 :
    print("Виграла Решка! \n")
    print(sum1)

elif sum == sum1 :
    print("Нічия.\n")
    print(sum)


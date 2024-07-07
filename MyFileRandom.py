import random

maxNum = 0

for a in range(16) :

    rund = random.randint(1, 100)
    print(rund)
    if rund > maxNum :
        maxNum = rund
print(maxNum)
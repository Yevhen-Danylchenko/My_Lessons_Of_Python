num = 0
sum = 0

while num <= 100 :
    print(num)
    num += 1
    if num % 2 == 0 :
        continue
    else:
        sum += num
print(sum)
num1 = int(input("Задайте число. \t"))
num2 = int(input("Задайте число. \t"))
num3 = int(input("Задайте число. \t"))
num4 = int(input("Задайте число. \t"))
num5 = int(input("Задайте число. \t"))
num6 = int(input("Задайте число. \t"))
num7 = int(input("Задайте число. \t"))

tmp = 0
tmp1 = 0
tmp2 = 0
tmp3 = 0
tmp4 = 0
tmp5 = 0

minTmp = 0
minTmp1 = 0
minTmp2 = 0

maxTmp = 0


if num1 > num2 :
    tmp = num1
elif num1 == num2 :
    tmp = num1
else: tmp = num2
if num2 > num3 :
    tmp1 = num2
elif num2 == num3 :
    tmp1 = num2
else: tmp1 = num3
if num3 > num4 :
    tmp2 = num3
elif num3 == num4 :
    tmp2 = num3
else: tmp2 = num4
if num4 > num5 :
    tmp3 = num4
elif num4 == num5 :
    tmp3 = num5
else: tmp3 = num5
if num5 > num6 :
    tmp4 = num5
elif num5 == num6 :
    tmp4 = num6
else: tmp4 = num6
if num6 > num7 :
    tmp5 = num6
elif num6 == num7 :
    tmp5 = num7
else: tmp5 = num7
if tmp > tmp1 :
    tmp = tmp
elif tmp == tmp1 :
    tmp = tmp
else: tmp = tmp1
if tmp2 > tmp3 :
    tmp2 = tmp2
elif tmp2 == tmp3 :
    tmp2 = tmp2
else: tmp2 = tmp3
if tmp4 > tmp5 :
    tmp4 = tmp4
elif tmp4 == tmp5 :
    tmp4 = tmp4
else: tmp4 = tmp5
if num6 > num7 :
    tmp5 = num6
elif num6 == num7 :
    tmp5 = num7
else: tmp5 = num7
if tmp > tmp2 :
    minTmp = tmp
elif tmp == tmp2 :
    minTmp = tmp
else: minTmp = tmp2
if tmp3 > tmp4 :
    minTmp1 = tmp3
elif tmp3 == tmp4 :
    minTmp1 = tmp4
else: minTmp1 = tmp4
if tmp4 > tmp5 :
    minTmp3 = tmp4
elif tmp4 == tmp5 :
    minTmp3 = tmp5
else: minTmp3 = tmp5
if minTmp > minTmp1 :
    minTmp = minTmp
elif minTmp == minTmp1 :
    minTmp = minTmp
else: minTmp = minTmp1
if minTmp2 > minTmp1 :
    minTmp2 = minTmp2
elif minTmp2 == minTmp1 :
    minTmp2 = minTmp2
else: minTmp2 = minTmp1
if minTmp3 > minTmp2 :
    minTmp3 = minTmp3
elif minTmp3 == minTmp2 :
    minTmp3 = minTmp3
else: minTmp3 = minTmp2
if minTmp > minTmp2 :
    maxTmp = minTmp
elif minTmp == minTmp2 :
    maxTmp = minTmp
else: maxTmp = minTmp2
if minTmp3 > minTmp2 :
    maxTmp = minTmp3
elif minTmp3 == minTmp2 :
    maxTmp = minTmp3
else: maxTmp = minTmp2
print(maxTmp)



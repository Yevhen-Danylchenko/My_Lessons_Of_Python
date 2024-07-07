num = int(input("Задайте число.\t"))

if num >= 1000 and num <= 9999 :
    num1 = num // 1000
    num2 = (num // 100) % 10
    num3 = (num // 10) % 10
    num4 = num % 10

    print(f"{num2}{num1}{num4}{num3}")

else: print("Невірне число.\n")
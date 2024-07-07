date = int(input("Enter Year \t"))

if date % 4 == 0 and date % 100 == 1 or date % 400 == 0:
    print("It's a leap year")
else: print("It's a not a leap year")

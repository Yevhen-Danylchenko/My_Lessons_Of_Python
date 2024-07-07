a = float(input("Enter first number"))     #Функція елс іф еліф
b = float(input("Enter second number"))
userChoise=str(input("Enter choise"))
if userChoise == "+":
    print(a+b)
elif userChoise == "-":
    print(a-b)
elif userChoise =="*":
    print(a*b)
elif userChoise=="/":
    if a==0 or b ==0 or a < b:
        print("Error")
    else:
        print(a/b)
else:
    print("Error")


amount = float(input("Enter sum\t"))

userInput=str(input("Enter code : EUR , DOL, PL\t"))

match userInput:
    case "EUR":
        print(amount * 44)
    case "DOL":
        print(amount*41)
    case "PL":
        print(amount*10)
    case _:
        print("You entered wrong code")
date = int(input("Enter number day of week\t"))

match date:                 #Функція матч кейс
    case 1:
        print("Понеділок")
    case 2:
        print("Вівторок")
    case 3:
        print("Середа")
    case 4:
        print("Четвер")
    case 5:
        print("П'ятниця")
    case 6:
        print("Субота")
    case 7:
        print("Неділя")
    case _:
        print("Error")
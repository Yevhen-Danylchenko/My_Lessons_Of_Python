month = int(input("Введіть число від одного до дванадцяти: \t"))

match month:

    case month if  month <= 2 and month == 12:
        print("Зараз зима. \n")
    case month if month <= 5 and month >= 3:
        print("Зараз весна. \n")
    case month if month <= 8 and month >=6:
        print("Зараз літо.\n")
    case month if month < 12 and month >=9:
        print("Зараз осінь. \n")
    case _:
        print("Неправильне число")
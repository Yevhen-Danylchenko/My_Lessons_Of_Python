date = str(input("Задайте назву дня неділі:\t"))

match date:
    case 'Понеділок':
        print("1")
    case 'Вівторок':
        print("2")
    case 'Середа':
        print("3")
    case 'Четвер':
        print("4")
    case 'Пятниця':
        print("5")
    case 'Субота':
        print("6")
    case 'Неділя':
        print("7")
    case _:
        print("Некоректно заданий день неділі!\n")
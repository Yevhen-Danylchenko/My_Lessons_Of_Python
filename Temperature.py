num = int(input("Задайте температуру від 0 до 30:\t"))

match num:
    case num if num >=0 and num < 5:
        print("Холодно.\n")
    case num if num >= 5 and num < 10:
        print("Прохолодно.\n")
    case num if num >=10 and num < 20:
        print("Тепло.\n")
    case num if num >=20 and num <=30:
        print("Жарко.\n")
    case _:
        print("Неправильно заданий показник температури!\n")
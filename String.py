userName = input('Введіть логін: \t')

if userName.lower() == 'admin' :
    print('Доступ дозволено.')
else :
    print('Доступ заборонено!')

print(userName.lower()) # Перетворює всі літери до маленьких
print(userName.upper()) # Перетворюе всі літери на великі.
print(userName.rstrip()) #Забірає пробіл праворуч
print(userName.lstrip()) #ліворуч
print(userName.strip()) #Забірає пробіли зліва та справа
print(userName.find()) #Повертає -1  якщо немає, якщо є то повертає індекс де воно знаходиться.
print(userName.replace()) # Заміняє один підрядок іншим
print(userName.split()) # Ділить рядок на підрядки
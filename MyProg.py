'''
a = 0
my_sum = 0

while a <= 100 :
    my_sum += a
    a+=1

print(my_sum)
'''

user = "admin"
userLogin = ""
num = 1

while userLogin != user :
    if num <= 3 :
        userLogin = str(input("Enter You Login. \t"))
        num += 1

    if num == 3 :
        print("Доступ заборонений!\n")
    break
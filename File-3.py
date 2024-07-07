list_of_numbres = [1, 4, 5, 6, 7, 1, 56, 1, 5, 1, 5, 9, 9, 5, 0, 0, 2]

new_list_of_numbers = []

for elements in list_of_numbres:
    if elements in new_list_of_numbers:
        continue
    else:
        new_list_of_numbers.append(elements)

list_of_numbres = new_list_of_numbers
new_list_of_numbers.clear()
print(list_of_numbres)

list_of_numbres=[1,4,5,6,7,1,56,1,5,1,5,9,9,5,0,0,2]

elem1 = list_of_numbres[0]

for index, elem in enumerate(list_of_numbres) :
    elem1 = elem[index+1]
    if elem == elem1 :
        list_of_numbres.pop(index)

print(list_of_numbres)
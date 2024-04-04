def removeNumber(str):
    tup = tuple(map(int,str[:-4].strip('()').split(',')))
    element = int(str[-2])
    newTuple = ()

    if element in tup and tup.count(element) > 1:
        index = tup.index(element)
        index2 = tup.index(element,index+1)
        newTuple = tup[index:index2+1]
    elif element in tup:
        index = tup.index(element)
        newTuple = tup[index:]

    return  tuple(newTuple)

one = '(1, 2, 3), 8)'
two = '(1, 8, 3, 4, 8, 8, 9, 2), 8)'
three = '(1, 2, 8, 5, 1, 2, 9), 8)'

print("one - ", removeNumber(one))
print("two - ", removeNumber(two))
print("three - ", removeNumber(three))

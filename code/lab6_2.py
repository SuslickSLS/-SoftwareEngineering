def removeNumber(str):
    tup = tuple(map(int,str[:-4].strip('()').split(',')))
    element = int(str[-2])
    newTuple = tup

    if element in tup:
        index = tup.index(element)
        newTuple = tup[:index] + tup[index + 1:]

    return  tuple(newTuple)

one = '(1, 2, 3), 1)'
two = '(1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)'
three = '(2, 4, 6, 6, 4, 2), 9)'

print("one - ", removeNumber(one))
print("two - ", removeNumber(two))
print("three - ", removeNumber(three))

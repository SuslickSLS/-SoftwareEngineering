def ultraSet(numbers):
    newNumbers = numbers
    for i in range(len(newNumbers)):
        count = numbers[i:].count(numbers[i])
        if(count == 1):
            newNumbers[i] = numbers[i]
        else:
            newNumbers[i] = str(numbers[i])*count


    return newNumbers


list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


print(ultraSet(list_1))
print(ultraSet(list_2))
print(ultraSet(list_3))

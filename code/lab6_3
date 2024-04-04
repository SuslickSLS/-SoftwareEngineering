def mostNumbers(text):
    count = len(text)
    a = list(map(int, text))
    dic = {i: a.count(i) for i in a}
    dic = dict(sorted(dic.items(), key=lambda item: item[0]))
    return dict(list(dic.items())[0:3])

numbers = input("Введите числа: ")
print(mostNumbers(numbers))

def Sum():
    try:
        userInput = float(input('Введите число: '))
        return userInput + 2
    except ValueError:
        return 'Не тот тип.'

print(Sum())
print(Sum())

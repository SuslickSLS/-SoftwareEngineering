userInput = input("Введите числа через пробел: ")

numbers = userInput.split()

print(numbers, " - ", type(numbers))
print(tuple(map(int, numbers)), " - ", type(tuple(map(int, numbers))))

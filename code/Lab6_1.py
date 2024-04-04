userInput = input("Введите числа через пробел: ")

numbers = userInput.split()

print(numbers, " - ", type(numbers))
print(tuple(numbers), " - ", type(tuple(numbers)))

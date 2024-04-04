userInput = input("Введите текс на English: ")

print(len(userInput))
print(userInput.lower())
print(userInput)


if userInput.__contains__("ugly"):
    print(userInput.replace("ugly", "beauty"))

if userInput.startswith("The"):
    print("Предложение начинается на The", end=" ")
else:
    print("Предложение не начинается на The", end=" ")

if userInput.endswith("end"):
    print("и заканчивается на end")
else:
    print("и не заканчивается на end")

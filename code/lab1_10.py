badWord= 'hello'
userInput = input("Введите текст: ")
print(userInput.replace(badWord,"*****").replace(badWord[0].upper()+badWord[1:], "*****"))
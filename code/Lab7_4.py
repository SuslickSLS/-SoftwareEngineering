import re

file = open('Lab7_4.txt','r',encoding='utf-8')
text = file.read()
banWords = text.split()

userInput = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... \nPYTHON is awesome!!!!"


for word in banWords:
    userInput = re.sub(word,lambda x: '*' * len(x.group()),userInput,flags=re.IGNORECASE)

print(userInput)

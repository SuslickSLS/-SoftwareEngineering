import re

file = open('Lab7_3.txt','r',encoding='utf-8')
text = file.read()
words = list(filter(lambda x: x != '',re.split("[ ,().—:«»'\n]",text)))

print("Кол-во букв: ", len(str.join(' ',words).replace(" ","")))
print("Кол-во слов: ", len(words))
print("Кол-во слов: ", len(text.split("\n")))

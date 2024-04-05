import re

file = open("Lab7_1.txt", 'r',encoding='utf-8')
words = list(filter(lambda x: x != '',re.split("[ ,().—:«»']",file.read())))



print("Кол-во слов: ", len(words))
print("Самое популярное слово: '", max(words, key=words.count), "' и встерчается ", words.count(max(words, key=words.count)), " раз")

def readFile(fileName):
    try:
        file = open(fileName,'r',encoding='utf-8')
        text = file.read()

        if not text:
            raise Exception("Пустой")

        print(text)
    except Exception as e:
        print(str(e))

readFile("Lab10_1_1.txt")
readFile("Lab10_1_2.txt")

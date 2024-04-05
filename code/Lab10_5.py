class GameError(Exception):
    def __init__(self, message):
        self.__message = message
        super().__init__(self.__message)


def Division(oneNumber,twoNumber):
    try:
       if(twoNumber == 0):
           raise GameError("Печаль")

       print(oneNumber/twoNumber)
    except GameError:
        print("Печаль ")

def GameLogin():
    try:
        username = input("Введите логин: ")
        password = input("Введите пароль: ")
        
        if username != "Suslick" or password != "12345":
            raise GameError("Неправильное имя или пароль:(.")
    except GameError :
        print("Неправильное имя или пароль:(")

Division(3,0)
Division(6,2)



GameLogin()
GameLogin()

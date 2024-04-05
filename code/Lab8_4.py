class Game:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating

    def get_name(self):
        return self.__name

    def get_rating(self):
        return self.__rating

class OnlineGame(Game):
    def __init__(self, name,countPeople, rating):
        super().__init__(name, rating)
        self.__countPeople = countPeople

    def get_countPeople(self):
        return self.__countPeople

game1 = Game("The last of us", 10)
print("Название игры: ", game1.get_name(), "\nРейтин metacritic: ", game1.get_rating())

game2 = OnlineGame("company of heroes 2 ", 2521, 8)
print("Название игры: ", game2.get_name(), "\nРейтин metacritic: ", game2.get_rating(), "\nКол-во игроков: ", game2.get_countPeople())

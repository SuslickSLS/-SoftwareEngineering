class Game:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating

    def get_name(self):
        return self.__name

    def get_rating(self):
        return self.__rating


game1 = Game("The last of us", 10)
print("Название игры: ", game1.get_name(), "\nРейтин metacritic: ", game1.get_rating())

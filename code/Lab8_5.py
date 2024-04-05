class Game:
    def __init__(self, name, rating):
        self.__name = name #private
        self.__rating = rating#private

    def get_name(self):
        return self.__name

    def get_rating(self):
        return self.__rating

    def set_name(self, name):
        self.__name = name

    def set_rating(self, rating):
        self.__rating = rating

class OnlineGame(Game):
    def __init__(self, name,countPeople, rating):
        super().__init__(name, rating)
        self.__countPeople = countPeople

    def get_countPeople(self):
        return self.__countPeople

game1 = Game("The last of us", 10)
print("Название игры: ", game1.get_name(), "\nРейтин metacritic: ", game1.get_rating())

game1.set_rating(100)

print("Название игры: ", game1.get_name(), "\nРейтин metacritic: ", game1.get_rating())

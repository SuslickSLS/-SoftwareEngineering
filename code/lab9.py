
#Создание класса Томаты
class Tomato:
    #Список зрелости томатов
    _states = ['отсутствует', 'цветение', 'зеленый', 'красный']

    # Установка начальных значений для томата
    def __init__(self, index):
        self._index = index
        self._state = Tomato._states[0]

    # Перевод томата на следующий этап
    def grow(self):
        if Tomato._states.index(self._state) <= 3:
            self._state = Tomato._states[Tomato._states.index(self._state) + 1]


    #Проверка на зрелость
    def is_ripe(self):
        return self._state == Tomato._states[3]

#Создание класса Томантный куст
class TomatoBush:

    # Установлеваем список всех томатов
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    # Перевод всех томатов на следующий этап
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверка на зрелость всех томатов
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    #Очистка куста
    def give_away_all(self):
        self.tomatoes = self.tomatoes.clear()


#Создание класса Садовник
class Gardener:

    # Установлеваем имя и растение
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Уход за растениями
    def work(self):
        self._plant.grow_all()
        print(f'{self.name} пашет по черному.')

    # Проверка спелости и сбор урожая. Если все спелые, то сбор урожая
    def harvest(self):
        if self._plant.all_are_ripe():
            print('Урожай созрел:)')
            self._plant.give_away_all()
        else:
            print('Томаты еще не созрели')

     # Функция справки по садовоству
    @staticmethod
    def knowledge_base():
        print('Справка по садоводству ')


tomatoBush = TomatoBush(5)
gardener = Gardener('Вася', tomatoBush)

Gardener.knowledge_base()

gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()

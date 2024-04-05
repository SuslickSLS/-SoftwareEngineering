class MyDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Выполнение функции ",self.func.__name__)

        result = self.func(*args, **kwargs)

        return result
@MyDecorator
def HelloPeople(firstName,lastName):
        return "Hello " + firstName + " " + lastName

@MyDecorator
def Addition():
    try:
        one = int(input('Введите первое значние: '))
        two = int(input('Введите второе значние: '))
        return "Сложение: " + str(one + two)
    except TypeError:
        return "Не тот тип"


firstName = input('Введите firstName: ')
lastName = input('Введите вlastName: ')

print(HelloPeople(firstName, lastName))
print(Addition())

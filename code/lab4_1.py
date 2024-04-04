from datetime import datetime
from math import sqrt


def main(**kwargs):
    """
    Функция выводит на консоль квадратный корень суммы квадратов двух чисел

    :param kwargs (dict): Принимает произвольное количество словарей

    Эта функция выводит сообщение на консоль и ничего не возвращает.
    """

    # пробегаем все элементы
    for key in kwargs.items():
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)

        # Выводим результат в консоль
        print(result)


# Точка входа в программу
if __name__ == '__main__':

    # Записываем в переменную время старта программы
    start_time = datetime.now()


    # Вызов функции main
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )

    # Подсчёт затраченного времени выполнения функции
    time_costs = datetime.now() - start_time

    # Вывод результат в консоль
    print(f"Время выполнения программы - {time_costs}")

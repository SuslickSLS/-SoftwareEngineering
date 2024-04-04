import random


def diceGame():
    rnd = random.randrange(1, 6)
    print('Выпало - %d' %rnd)

    if rnd >= 5:
        print('Вы выйграли:)')
    elif 3 <= rnd <= 4:
        diceGame()
    elif 1 <= rnd <= 2:
        print('Вы проиграли:(')


if __name__ == '__main__':
    diceGame()

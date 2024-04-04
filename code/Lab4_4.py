def meanArithmetic(**kwargs):
    for key, value in kwargs.items():
        print("Среднее арифметическое: %f" %(sum(value) / float(len(value))))


if __name__ == '__main__':
    meanArithmetic(
        one = [3, 8, 12],
        two = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    )

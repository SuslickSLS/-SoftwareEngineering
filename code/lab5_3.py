def areaTriagle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        return 0

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

maxNumber = 0
minNumber = max(one)

for value in itertools.product(one, two, three):
    number = areaTriagle(value[0], value[1], value[2])

    if(number > maxNumber):
        maxNumber = number


    if(number < minNumber and number != 0):
        minNumber = number


print("Максимальная площадь треугольника:", maxNumber)
print("Минимальная площадь треугольника:", minNumber)

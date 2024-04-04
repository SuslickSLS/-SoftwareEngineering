from math import sqrt

def triangleGerona(a, b, c):

    p = (a+b+c)/2

    return sqrt(p*(p-a)*(p-b)*(p-c))

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

print("Площадь треугольника = %f" %triangleGerona(a, b, c))

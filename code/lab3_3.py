try:
    userNumber = int(input("Введите число в диапозоне 0 - 10: "))
    if 0 <= userNumber <= 3: print("Число в диапозоне от 0 до 3 вкл.")
    elif 4 <= userNumber <= 6: print("Число в диапозоне от 3 до 6 вкл.")
    elif 7 <= userNumber <= 10: print("Число в диапозоне от 6 до 10 вкл.")
    else: print("Невверный диапозон")
except ValueError: print("Не число:)")

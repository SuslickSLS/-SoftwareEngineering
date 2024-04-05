def add_expense(date, category, amount):
    with open('Lab7_2.txt', 'a') as file:
        file.write(f"{date},{category},{amount}\n")
    print("Расход успешно добавлен.")


def display_expenses():
    with open('Lab7_2.txt', 'r') as file:
        for line in file:
            print(line.strip())


open('Lab7_2.txt', 'a').close()
isExit = False
while isExit == False:
    print("1. Добавить расход")
    print("2. Вывести все расходы")
    print("3. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        date = input("Введите дату расхода: ")
        category = input("Введите категорию расхода: ")
        coast = input("Введите сумму расхода: ")

        add_expense(date, category, coast)

    elif choice == '2':
        print("Существующие расходы:")
        display_expenses()

    elif choice == '3':
        isExit = True

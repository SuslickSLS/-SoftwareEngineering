def add_dossier(dossiers):
    key = input("Введите ФИО.: ")
    value = input("Введите Должность: ")
    dossiers[key] = value


def show_all_dossier(dossiers):
    for key, value in dossiers.items():
        print(f"{key}: {value}")


dossiers = {}
isExit = True

while isExit:

    print("1) Добавить досье \n"
          "2) Показать все досье \n"
          "3) Выйти")
    try:
        userInput = int(input("Введите номер: "))
    except ValueError:
        userInput = 0

    if userInput == 1:
        add_dossier(dossiers)

    elif userInput == 2:
        show_all_dossier(dossiers)

    elif userInput == 3:
        isExit = False

    else:
        print("Неверный код")

    print()

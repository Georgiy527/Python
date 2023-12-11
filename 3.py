class NotANumberError(Exception):
    pass


number_list = []

while True:
    try:
        user_input = input("Введите число (или 'stop' для завершения): ")

        if user_input.lower() == 'stop':
            break

        number = int(user_input)
        number_list.append(number)
    except ValueError:
        print("Ошибка: Введенное значение не является числом. Повторите попытку.")
    except NotANumberError:
        print("Ошибка: Введенное значение не является числом. Повторите попытку.")

print(number_list)

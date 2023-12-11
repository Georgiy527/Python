class DivisionByZeroError(Exception):
    def __init__(self, message="Деление на ноль недопустимо"):
        self.message = message
        super().__init__(self.message)

def divide_numbers(a, b):
    if b == 0:
        raise DivisionByZeroError
    return a / b

# Проверка работы класса
try:
    numerator = int(input("Введите числитель: "))
    denominator = int(input("Введите знаменатель: "))
    result = divide_numbers(numerator, denominator)
    print(f"Результат деления: {result}")
except DivisionByZeroError as e:
    print(e)
except ValueError:
    print("Ошибка. Введите числовое значение")

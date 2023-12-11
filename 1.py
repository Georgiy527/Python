class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def parse_date(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        return cls(day, month, year)

    @staticmethod
    def validate_date(date_str):
        day, month, year = map(int, date_str.split('-'))
        if day < 1 or day > 31:
            return False
        if month < 1 or month > 12:
            return False
        if year < 1900 or year > 2100:
            return False
        return True

# Проверка работы класса
date_str = "10-12-2023"
if Date.validate_date(date_str):
    d = Date.parse_date(date_str)
    print(f"День: {d.day}, Месяц: {d.month}, Год: {d.year}")
else:
    print("Некорректная дата")

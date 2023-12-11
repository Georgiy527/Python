class Warehouse:
    def __init__(self):
        self.inventory = {} # словарь для хранения наименования и количества оргтехники на складе

    def receive_item(self, item, quantity):
        if isinstance(quantity, int) and quantity > 0:
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity
            print(f"Принято на склад {quantity} единиц оргтехники {item.brand} - {item.model}")
        else:
            print("Некорректное количество оргтехники")

    def send_item(self, item, quantity, department):
        if item in self.inventory and self.inventory[item] >= quantity:
            if isinstance(quantity, int) and quantity > 0:
                self.inventory[item] -= quantity
                print(f"Передано в подразделение '{department}' {quantity} единиц оргтехники {item.brand} - {item.model}")
            else:
                print("Некорректное количество оргтехники")
        else:
            print("Недостаточно оргтехники на складе")

class OfficeEquipment:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, is_color):
        super().__init__(brand, model, price)
        self.is_color = is_color

class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, max_resolution):
        super().__init__(brand, model, price)
        self.max_resolution = max_resolution

class Copier(OfficeEquipment):
    def __init__(self, brand, model, price, paper_capacity):
        super().__init__(brand, model, price)
        self.paper_capacity = paper_capacity

# Пример использования
warehouse = Warehouse()
printer_1 = Printer("Epson", "L3150", 300, True)
printer_2 = Scanner("HP", "1010", 150, True)
warehouse.receive_item(printer_1, 5) #Принято на склад 5 единиц оргтехники 'L3150'
warehouse.receive_item(printer_2, 1)
warehouse.send_item(printer_1, 2, "Отдел продаж") # Передано в подразделение 'Отдел продаж' 2 единицы оргтехники 'L3150'
warehouse.send_item(printer_2, 1, "Бухгалтерии")
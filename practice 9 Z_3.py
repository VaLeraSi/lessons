class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._Worker__income.values())}"


employee = Position("IVAN", "KNOWN", "MANAGER", 50000, 8000)
print(employee.get_full_name())
print(employee.position)
print(employee.get_full_profit())

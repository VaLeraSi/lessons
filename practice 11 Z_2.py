class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите число, отличное от нуля: ")
inp_data_2 = input("Введите число, отличное от нуля: ")
try:
    inp_data = int(inp_data)
    inp_data_2 = int(inp_data_2)
    result = int(inp_data) // int(inp_data_2)
    if inp_data_2 == 0:
        raise ZeroError("Вы ввели 0!")
except ZeroError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше результат: {result}")

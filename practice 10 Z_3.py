class Cell:
    def __init__(self, nums):
        self.nums = nums

    # def make_order(self, rows):
    #     return "\n".join(['+' * rows for _ in range(self.nums // rows)]) + "\n" + "*" * (self.nums % rows)
    # не очень поняла функционал этой части кода

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("SUM:")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("SUB:")
        return Cell(self.nums - other.nums)

    def __mul__(self, other):
        print("MUL:")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("DIV:")
        return Cell(self.nums // other.nums)


cell_1 = Cell(12)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)

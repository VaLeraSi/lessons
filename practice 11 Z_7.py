class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.sumax = self.x + other.x
        self.sumay = self.y + other.y

    def __mul__(self, other):
        self.multx = self.x * other.x - self.y * other.y
        self.multy = self.y * other.x + self.x * other.y


x = float(input())
y = float(input())
a = Complex(x, y)
x = float(input())
y = float(input())
b = Complex(x, y)
a + b
a * b
print('Сумма: %.2f+%.2fj' % (a.sumax, a.sumay))
print('Произв.: %.2f+%.2fj' % (a.multx, a.multy))

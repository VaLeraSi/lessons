a = [[1, 2, 3], [4, 5, 6]]
b = [[4, 5, 6], [1, 2, 3]]


class Matrix:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return '\n'.join(map(str, self.param))

    def __add__(self, other):
        c = []
        for i in range(len(self.param)):
            c.append([])
            for j in range(len(self.param[0])):
                c[i].append(self.param[i][j] + other.param[i][j])
        return '\n'.join(map(str, c))


mx_1 = Matrix(a)
mx_2 = Matrix(b)
print(mx_1.param)
print(mx_2.param)
print(f"Matrix 1\n{mx_1}")
print(f"Matrix 2\n{mx_2}")
print(f"Matrix 1 + Matrix 2\n{mx_1 + mx_2}")

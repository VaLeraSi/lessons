class Stationery:
    def __init__(self, title="The first page"):
        self.title = title

    def draw(self):
        print(f"Please, start drawing {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Please, start drawing with a {self.title} pen")


class Pencil(Stationery):
    def draw(self):
        print(f"Please, start drawing with a {self.title} pencil")


class Handle(Stationery):
    def draw(self):
        print(f"Please, start drawing with a {self.title} handle")


start = Stationery()
start.draw()
pen = Pen("black")
pen.draw()
pencil = Pencil("blue")
pencil.draw()
handle = Handle("red")
handle.draw()

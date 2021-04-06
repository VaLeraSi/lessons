from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Suit(0)

    def __str__(self):
        Clothes.result = 0
        return f"{Clothes.result}"


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


class Suit(Clothes):
    @property
    def consumption(self):
        return round(self.param * 2 + 0.3) / 100


coat = Coat(42)
suit = Suit(175)
print(coat + suit)

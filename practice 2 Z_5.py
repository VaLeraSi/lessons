print("-" * 40,"A/B")

prices = [56.4, 89.01, 132.5, 33.02, 44.1, 1052.06, 333, 1.5, 11.22, 222]
for i in prices:
    r = int(i // 1)
    k = int(f"{i % 1:.02f}"[2:])
    prices.sort()
    print(f"{r:02d} руб {k:02d} коп") # не пойму, почему 56 руб 40 коп выводится дважды

print("-" * 40, "C")

prices = [56.4, 89.01, 132.5, 33.02, 44.1, 1052.06, 333, 1.5, 11.22, 222]
for i in prices:
    r = int(i // 1)
    k = int(f"{i % 1:.02f}"[2:])
    prices.sort(reverse=True)
    print(f"{r:02d} руб {k:02d} коп") # пропало значение 1052.06...

# Почему при выводе первое значение всегда заменяется на 56.40?

print("-" * 40, "D")


prices = [56.4, 89.01, 132.5, 33.02, 44.1, 1052.06, 333, 1.5, 11.22, 222]
for i in prices:
    r = int(i // 1)
    k = int(f"{i % 1:.02f}"[2:])
    prices.sort()
    print(prices[-5:]) # Как вывести только одну строку?

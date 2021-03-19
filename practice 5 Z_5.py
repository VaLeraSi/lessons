src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_number = [i for i in src if src.count(i) == 1]
print(unique_number)

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_number = set()
tmp = set()
for i in src:
    if i not in tmp:
        unique_number.add(i)
    else:
        unique_number.discard(i)
    tmp.add(i)
unique_number_ord = [i for i in src if i in unique_number]
print(unique_number_ord)

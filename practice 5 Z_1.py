def nums(n):
    for num in range(1, n + 1, 2):
        yield num


for i in nums(55):
    print(i)
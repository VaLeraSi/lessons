with open("nginx_logs.txt", "r", encoding="utf-8") as file_1:
    text = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in file_1)
    for i in text:
        print(i)

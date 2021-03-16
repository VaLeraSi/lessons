from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:

        first_list = zip_longest((" ".join(i.split(',')) for i in users), hobby, fillvalue=None)
        full_list = {str(j[0]).strip(): (j[1].strip()) for j in first_list}

        with open("full_list.json", "w", encoding="utf-8") as f:
            dump(full_list, f, ensure_ascii=False, indent=4)
            print(full_list)

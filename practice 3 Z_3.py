def thesaurus(*names):
    name_dict = {}
    for i in names:
        key = i[0].capitalize()
        if key not in name_dict:
            name_dict[key] = [i]
        else:
            name_dict[key].append(i)

    return name_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Мирон"))

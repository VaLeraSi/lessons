from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Кирилл', 'Светлана']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
new_gen = ((i for i in zip_longest(tutors, klasses)))

print(type(new_gen))
print(*new_gen)

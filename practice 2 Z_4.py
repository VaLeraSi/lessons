position = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
            'директор аэлита']
for a in position:
    a.split()[-1].title()
    print(f"Привет, {a.split()[-1].title()}!")
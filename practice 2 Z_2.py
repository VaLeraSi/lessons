weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
weather[1] = '"5"'
weather[3] = '"17"'
weather[-2] = '"+5"'
for i, a in enumerate(weather):
    if a.replace("+", "").replace("-", "").isdigit():
        if a.isdigit():
            weather[i] = f'{int(a):02}'
        else:
            weather[i] = f'{a[0]}{int(a[1:]):02}'

print(" ".join(weather))

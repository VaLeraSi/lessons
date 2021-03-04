from random import choice


def get_jokes(repeat=False):
    """
    Функция формирует случайные шутки, собранные из трех слов трех списков
    :return: возвращает шутку
    :param repeat: повторение слов в шутках
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []
    joke.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
    return joke


print(get_jokes(True))

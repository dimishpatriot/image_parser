def yes_or_no(answer):
    """
    проверка на согласие
    :param answer: ответ str
    :return: True/False
    """
    d = ('y', 'Y', 'yes', 'Yes', 'YES')
    yes = False
    if d.count(answer):
        yes = True
    return yes


def is_num(num, min_value=0, max_value=100):
    """
    проверка на число (через try) и на диапазон числа, при необходимости
    :param num: строкой или числом
    :param min_value: минимальное значение, по-умолчанию 0
    :param max_value: максимальное значение, по-умолчанию 100
    :return: True/False
    """
    ans = False
    try:
        if min_value <= int(num) <= max_value:  # Одновременная проверка на диапозон и на int
            ans = True
    except:
        ans = False
    return ans


def link_is_pic(link):
    """
    проверка, является ли ссылка, ссылкой на картинку определенных форматов
    :param link: ссылка http
    :return: True/False через 0/1
    """
    ext_dict = ('jpg', 'jpeg', 'png', 'gif')  # список возможных расширений
    ext = link.split('.')[-1]  # разделение ссылки по точке, первое с конца - расширение (практически всегда)

    if ext_dict.count(ext) > 0:
        ans = True
    else:
        ans = False

    return ans

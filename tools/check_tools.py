# -*- coding: utf-8 -*-
# check_tools.py
# github.com/dimishpatriot/img_pars

def yes_or_no(answer):
    """
    проверка на согласие
    :param answer: ответ str
    :return: True/False
    """
    d = ('y', 'Y', 'yes', 'Yes', 'YES', 'ДА', 'да', 'Д', 'д', 'Да')
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
        # Одновременная проверка на диапозон и на int
        if min_value <= int(num) <= max_value:
            ans = True
    except:
        ans = False
    return ans

def link_is_pic(url):
    pic_ext = ("jpg", "jpeg", "png", "tiff", "bmp", 
               "gif", "pcx", "epf", "ico", "cdr",
              "svg")
    ext = url.split('.')[-1]
    if ext in pic_ext:
        return True
    else:
        return False
    

# -*- coding: utf-8 -*-
# useragent_tools.py
# github.com/dimishpatriot/img_pars

from random import choice


def get_useragent(path: str) -> dict:
    """
    получение случайного Useragent из файла
    :return:
    """
    print("Выбираю подменный user-agent...")
    try:
        ua_list = open(path + "/lists/useragents_list.txt").read().split("\n")
        user_agent = {"User-Agent": choice(ua_list)}
        print("+ user-agent успешно выбран", user_agent)
    except FileNotFoundError:
        user_agent = None
        print("- user-agent не выбран, скорее всего, что то с файлом")
    return user_agent

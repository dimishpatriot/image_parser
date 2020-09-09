# -*- coding: utf-8 -*-
# main.py
# github.com/dimishpatriot/img_pars

import os
from downloading import download_machine
from searching import search_by_google
from searching import search_by_yandex
from tools import file_tools, html_tools, imaging_tools
from tools import proxy_tools, check_tools, useragents_tools


class Program:
    def __init__(self):
        self.name = "ImageSearchDownloadMachine (ISDM)"
        self.version = "0.1 beta"
        self.author = "dimishpatriot@github.com"
        self.rep = "https://github.com/dimishpatriot/img_pars"
        self.path = os.getcwd()


def search_start(obj):
    """
    запуск поисковой машины
    :param obj: объект поиска класса YandexSearch или иного
    """
    folder_to = file_tools.get_result_folder_name(obj)  # полный путь
    file_tools.make_dir(folder_to)  # проверяется и создается папка

    print("Пробую сменить прокси...")
    new_proxy = proxy_tools.get_proxy(obj.path)  # подмена прокси
    new_user_agent = useragents_tools.get_useragent(
        obj.path)  # подмена useragent

    if obj.__class__ is search_by_yandex.YandexSearch:  # пока реализован только яндекс-поиск
        obj.links = search_by_yandex.YandexSearch.html_yandex(
            obj,
            proxy=new_proxy,
            user_agent=new_user_agent)
    elif obj.__class__ is search_by_google.GoogleSearch:  # зарезервировано по гугл
        pass
    obj.urls_list = html_tools.clear_links(obj)


def download_start(obj):
    """
    запуск машины для скачивания
    :param obj: объект ранее созданный поиском
    """
    print("Теперь, ответь еще на 2 вопроса:".center(80))

    print("1. Хочешь скачать изображения по найденным ссылкам? (y/n)")
    if check_tools.yes_or_no(input(">  ")):
        print("2. Хочешь использовать многопоточное скачивание? Это гораздо быстрее, но может быть не стабильно (y/n)")
        # согласие на многопоточное скачивание
        multi = check_tools.yes_or_no(input(">  "))
        print(imaging_tools.line_separator)  # ---
        # инициализация машины для скачивания и запуск скачивания
        dm = download_machine.DM(obj)

        if multi:
            dm.multi_way()
        elif not multi:
            dm.one_way()

        print(imaging_tools.line_separator)  # ----
        print("Всего выбрано ссылок: ", dm.all_links)
        print("Успешно скачано: ", dm.success_links)

    else:  # отказ от скачивания
        print(imaging_tools.line_separator)  # ---
        print("Скачки отменяются!")
        imaging_tools.bye_bye()


# START
if __name__ == "__main__":
    program = Program()
    imaging_tools.welcome(program)  # вступление
    search_machines = {"title": "Выбери поисковую машину:",
                       1: "Yandex.ru",
                       2: "Google.com (пока не реализовано :)",
                       0: "Выход из приложения"}

    mach = imaging_tools.cons_menu(search_machines)

    if mach == 1:
        s_object = search_by_yandex.YandexSearch(program.path)
        search_start(s_object)  # инициализация поисковой машины
    if mach == 2:
        print("Поиск по Google пока не работает (см.выше). Запускаю Yandex :)\n")
        # s_object = search_by_google.GoogleSearch(program.path)
        s_object = search_by_yandex.YandexSearch(program.path)
        search_start(s_object)  # инициализация поисковой машины

    print(imaging_tools.line_separator)  # ---

    if len(s_object.urls_list) > 0:  # если что-то есть в урлах, предложение закачать
        download_start(s_object)
    else:
        print("Нечего скачивать. Прости и попробуй позднее")

    imaging_tools.bye_bye()  # прощание

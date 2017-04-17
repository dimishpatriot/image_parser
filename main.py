#!/usr/bin/python3
# -*- coding: utf-8 -*-

import check_tools  # верификация ответов
import download_machine  # машина для закачки
import file_tools
import imaging_tools  # красоты там :)
import program_data  # данные программы
import proxy_tools
import search_by_google
import search_by_yandex
import search_main  # работа с запросами
import useragents_tools


def search_start(obj):
    """
    запуск поисковой машины
    :param obj: объект поиска класса YandexSearch или иного
    """
    folder_to = file_tools.get_folder_name(obj.text)  # полный путь
    file_tools.make_dir(folder_to)  # проверяется и создается папка

    new_proxy = proxy_tools.get_proxy()  # подмена прокси

    new_user_agent = useragents_tools.get_useragent()  # подмена useragent

    if obj.machine == obj.search_machines[1]:  # пока реализован только яндекс-поиск
        search_by_yandex.YandexSearch.html_yandex(
            obj,
            proxy=new_proxy,
            user_agent=new_user_agent,
            folder_to_save=folder_to)

    elif obj.machine == obj.search_machines[2]:  # зарезервировано по гугл
        pass

    elif obj.machine == obj.search_machines[3]:  # зарезервировано под что-то еще
        pass


def download_start(obj):
    """
    запуск машины для скачивания
    :param obj: объект ранее созданный поиском
    """
    print('And now, answer 2 questions more:')

    print('Would you like to download the links found? (Y/any)')
    if check_tools.yes_or_no(input('# ')):
        print('Would you like try multi-threading-download? Faster, may be not stable (Y/any)')
        multi = check_tools.yes_or_no(input('# '))  # согласие на многопоточное скачивание

        imaging_tools.split_line()  # ---

        dm = download_machine.DM(search_text=obj.text)  # инициализация машины для скачивания и запуск скачивания

        if multi:
            dm.multi_way()
        elif not multi:
            dm.one_way()

        imaging_tools.split_line()  # ----
        print('all links: ', dm.all_links)
        print('success links: ', dm.success_links)

    else:  # отказ от скачивания
        imaging_tools.split_line()  # ---
        print('Downloading abort!')


# START
if __name__ == '__main__':

    imaging_tools.welcome(program_data.Program())  # вступление

    sm = search_main.Search().machine_num  # выбор машины для поиска
    if sm == 1:
        s_object = search_by_yandex.YandexSearch()
        search_start(s_object)  # инициализация поисковой машины
    if sm == 2:
        s_object = search_by_google.GoogleSearch()
    if sm == 3:
        pass

    imaging_tools.split_line()  # ---

    if len(s_object.urls_list) > 0:  # если что-то есть в урлах, предложение закачать
        download_start(s_object)

    else:
        print('Nothing to download. Sorry & try later')

    imaging_tools.bye_bye()  # прощание

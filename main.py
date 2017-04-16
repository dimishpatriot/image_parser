#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

import check_tools  # верификация ответов
import download_machine  # машина для закачки
import file_tools
import imaging_tools  # красоты там :)
import inquiry  # работа с запросами
import program_data  # данные программы
import proxy_tools
import search_by_yandex
import useragents_tools


def search_start(obj, folder, machine):
    folder_to = os.getcwd() + folder  # полный путь

    file_tools.make_dir(folder_to)  # проверяется и создается папка

    new_proxy = proxy_tools.get_proxy()  # подмена прокси
    new_user_agent = useragents_tools.get_useragent()  # подмена useragent

    if machine == 1:
        search_by_yandex.YandexSearch.html_yandex(
            obj,
            proxy=new_proxy,
            user_agent=new_user_agent,
            folder_to_save=folder_to)
    elif machine == 2:
        pass


def download_start(obj, folder):
    print('And now, answer 2 questions more:')

    print('Would you like to download the links found? (Y/N)')
    if check_tools.yes_or_no(input('# ')):

        print('Would you like try multi-threading-download? Faster, may be not stable (Y/N)')
        if check_tools.yes_or_no(input('# ')):
            multi = 1
        else:
            multi = 0

        imaging_tools.split_line()  # ---

        print('Downloading begins to {} ...'.format(folder))
        my_download = download_machine.DM(
            search_text=obj.text,
            folder=folder,
            multi_dwn=multi)  # инициализация машины для скачивания и запуск скачивания

    else:
        imaging_tools.split_line()  # ---

        print('Downloading abort!')


# START
if __name__ == '__main__':

    imaging_tools.welcome(program_data.Program())  # вступление

    s_machine = inquiry.Search()  # выбор поисковой машины

    if s_machine.machine_num == 1:
        s_object = search_by_yandex.YandexSearch()
        folder_to_save = file_tools.get_folder_name(s_object.text)  # папка для записи
        imaging_tools.split_line()  # ---

        search_start(s_object, folder=folder_to_save, machine=s_machine.machine_num)  # инициализация поисковой машины
        imaging_tools.split_line()  # ---

    if len(s_object.urls_list) > 0:
        download_start(s_object, folder=folder_to_save)

    else:
        print('Nothing to download. Sorry & try later')

    imaging_tools.bye_bye()

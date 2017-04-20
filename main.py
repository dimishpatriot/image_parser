#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from downloading import download_machine
from searching import search_by_google
from searching import search_by_yandex
from tools import file_tools
from tools import imaging_tools, proxy_tools, check_tools
from tools import useragents_tools


class Program:
    def __init__(self):
        self.name = 'ImageSearchDownloadMachine (ISDM)'
        self.version = '0.1.1'
        self.author = 'dimishpatriot'
        self.rep = 'https://github.com/dimishpatriot/img_pars.git'
        self.path = os.getcwd()


def search_start(obj, machine):
    """
    запуск поисковой машины
    :param obj: объект поиска класса YandexSearch или иного
    """
    folder_to = file_tools.get_result_folder_name(obj)  # полный путь
    file_tools.make_dir(folder_to)  # проверяется и создается папка

    new_proxy = proxy_tools.get_proxy(obj.path)  # подмена прокси

    new_user_agent = useragents_tools.get_useragent(obj.path)  # подмена useragent

    if machine == 1:  # пока реализован только яндекс-поиск
        search_by_yandex.YandexSearch.html_yandex(
            obj,
            proxy=new_proxy,
            user_agent=new_user_agent)

    elif machine == 2:  # зарезервировано по гугл
        pass

    elif machine == 3:  # зарезервировано под что-то еще
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

        dm = download_machine.DM(obj)  # инициализация машины для скачивания и запуск скачивания

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

    pr = Program()

    imaging_tools.welcome(pr)  # вступление

    search_machines = {0: 'Select search machine:',
                       1: 'Yandex.ru',
                       2: 'Google.com (not realised yet :)'}

    mach = imaging_tools.cons_menu(search_machines)

    if mach == 1:
        s_object = search_by_yandex.YandexSearch(pr.path)
        search_start(s_object, mach)  # инициализация поисковой машины
    if mach == 2:
        s_object = search_by_google.GoogleSearch(pr.path)
    if mach == 3:
        pass

    imaging_tools.split_line()  # ---

    if len(s_object.urls_list) > 0:  # если что-то есть в урлах, предложение закачать
        download_start(s_object)

    else:
        print('Nothing to download. Sorry & try later')

    imaging_tools.bye_bye()  # прощание

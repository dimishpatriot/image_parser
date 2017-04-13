#!/usr/bin/python3
# -*- coding: utf-8 -*-

import imaging_tools  # красоты там :)
import machine_search  # поисковая машина
import machine_download  # машина для закачки
import test_tools  # верификация ответов
import file_tools  # работа с файлами

# START


if __name__ == '__main__':
    version = '0.1'
    rep = 'https://github.com/dimishpatriot/img_pars.git'
    imaging_tools.welcome(
        version=version,
        repository=rep)

    print('First, answer 2 questions:')
    search_text = input('1. What are you looking for? ')

    while True:
        n_pict = input('2. How many pictures you need? ')

        if not test_tools.is_num(n_pict):
            print('Input correct value!')
        else:
            break

    num = int(n_pict)

    imaging_tools.split_line()  # ---

    folder_to_save = file_tools.folder_to_save(search_text)

    my_search = machine_search.SM(
        search_text=search_text,
        num_pics=num,
        folder=folder_to_save)  # инициализация поисковой машины
    my_search.search_links()

    imaging_tools.split_line()  # ---

    if len(my_search.urls_list) > 0:
        print('And now, answer 2 questions more:')

        if test_tools.yes_or_no(input('3. Would you like to download the links found? (Y/N) ')):
            if test_tools.yes_or_no(input('4. Would you like try multi-threading-download? (Y/N) ')):
                multi = 1
            else:
                multi = 0

            imaging_tools.split_line()  # ---

            print('Downloading begins to {} ...'.format(folder_to_save))
            my_download = machine_download.DM(
                search_text=search_text,
                folder=folder_to_save,
                multi_dwn=multi)  # инициализация машины для скачивания и запуск скачивания

        else:
            imaging_tools.split_line()  # ---

            print('Downloading abort!')
    else:
        print('Nothing to download. Sorry & try later')

    imaging_tools.bye_bye()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import program_data  # данные программы
import imaging_tools  # красоты там :)
import search_machine  # поисковая машина
import download_machine  # машина для закачки
import test_tools  # верификация ответов
import file_tools  # работа с файлами
import inquiry_tools  # работа с запросами

# START


if __name__ == '__main__':

    program=program_data.Program()

    imaging_tools.welcome(
        program_name=program.name,
        version=program.version,
        repository=program.rep,
        author=program.author)

    # TODO добавить выбор простого запроса (только текст и 10 картинок на выходе) или сложного с параметрами

    print('First, answer 2 questions:')
    search_text = input('1. What are you looking for? ')

    while True:
        n_pict = input('2. How many pictures you need? ')

        if not test_tools.is_num(n_pict):
            print('Input correct value!')
        else:
            break
    num = int(n_pict)
    # TODO добавить выбор размера картинок
    # TODO добавить выбор типа картинок
    # TODO добавить выбор цветовой гаммы
    # TODO Добавить выбор ориентации
    imaging_tools.split_line()  # ---

    folder_to_save = file_tools.folder_to_save(search_text)

    my_search = search_machine.SM(
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
            my_download = download_machine.DM(
                search_text=search_text,
                folder=folder_to_save,
                multi_dwn=multi)  # инициализация машины для скачивания и запуск скачивания

        else:
            imaging_tools.split_line()  # ---

            print('Downloading abort!')
    else:
        print('Nothing to download. Sorry & try later')

    imaging_tools.bye_bye()

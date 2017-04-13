#!/usr/bin/python3
# -*- coding: utf-8 -*-

import imaging  # красоты там :)
import machine_search  # поисковая машина
import machine_download  # машина для закачки
import test_ans  # верификация ответов

# START


if __name__ == '__main__':
    version = '0.1'
    rep = 'https://github.com/dimishpatriot/img_pars.git'
    imaging.welcome(version=version, repository=rep)

    print('First, answer a few questions:')
    text = input('1. What are you looking for? ')

    ans = False
    n_pict = 0

    while not ans:
        n_pict = input('2. How many pictures you need? ')
        ans = test_ans.is_num(n_pict)
        if not ans:
            print('Input correct value!')
    num = int(n_pict)

    my_search = machine_search.SM(search_text=text, num_pics=num)  # инициализация поисковой машины
    my_search.search_links()

    imaging.split_line()

    if len(my_search.urls_list) > 0:

        ans = False
        dwn = input('Would you like to download the links found? (Y/N) ')
        ans = test_ans.yes_or_no(dwn)
        if ans:
            folder_to_save = '/search_result/' + '_'.join(text.split(' ')) + '/'  # имя папки для сохранения
            print('Downloading begins to {} ...'.format(folder_to_save))
            my_download = machine_download.DM(url_list=my_search.urls_list,
                                              folder=folder_to_save)  # инициализация машины для скачивания
            my_download.downloader()
        else:
            print('Downloading abort!')
    else:
        print('Nothing to download. Sorry & try later')

    imaging.bye_bye()

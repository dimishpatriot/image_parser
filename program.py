# -*- coding: utf-8 -*-
# program.py
# github.com/dimishpatriot/img_pars

import os
from downloading import download_machine
from searching import search_by_google
from searching import search_by_yandex
from tools import html_tools, imaging_tools, file_tools
from tools import proxy_tools, check_tools, useragents_tools


class Program:
    def __init__(self):
        self.name = "Image Search Download Machine (ISDM)"
        self.version = "0.1 beta"
        self.author = "dimishpatriot@github.com"
        self.rep = "https://github.com/dimishpatriot/img_pars"
        self.path = os.getcwd()

    def search_start(self, search):
        folder_name = "_".join(search.text.split())
        folder_to = f"{self.path}/search_result/{folder_name}/"
        if not os.path.exists(folder_to):  # проверка на наличие папки
            os.makedirs(folder_to)  # создание папки

        # подмена прокси
        new_proxy = proxy_tools.get_proxy(self.path)
        # подмена useragent
        new_user_agent = useragents_tools.get_useragent(self.path)

        if search.__class__ is search_by_yandex.YandexSearch:
            raw_links = search_by_yandex.YandexSearch.get_full_links(
                search,
                proxy=new_proxy,
                user_agent=new_user_agent)
        elif search.__class__ is search_by_google.GoogleSearch:  # зарезервировано
            pass

        search.clear_urls = html_tools.clear_links(raw_links)
        search.num_links = len(search.clear_urls)

        if search.num_links > 0:
            print(f"\n+ Лист ссылок сформирован из {search.num_links} шт.")
        else:
            print("- Лист ссылок пуст!")
            print("Нечего скачивать. Прости и попробуй позднее")
            imaging_tools.bye_bye()

        file_tools.save_links_to_file(search.clear_urls,
                                      search.results_path)
        print(f"+ Лист записан в файл > {search.results_path}/urls_list.txt")

    def download_start(self, search):
        """
        запуск машины для скачивания
        :param search: объект ранее созданный поиском
        """
        print()
        print(" Еще на 2 вопроса: ".center(80, '.'))

        print("1. Хочешь скачать изображения по найденным ссылкам? (y/n)")
        if check_tools.yes_or_no(input(">  ")):
            print("2. Хочешь использовать многопоточное скачивание? Это гораздо быстрее, но может быть не стабильно (y/n)")

            # согласие на многопоточное скачивание
            multi = check_tools.yes_or_no(input(">  "))
            print(imaging_tools.line_separator)  # ---

            # инициализация машины для скачивания и запуск скачивания
            dm = download_machine.DM(search.results_path,
                                     search.text)

            if multi:
                success_downloads = dm.multi_way(search.clear_urls)
            elif not multi:
                success_downloads = dm.one_way(search.clear_urls)

            print(imaging_tools.line_separator)  # ----
            print(f"Всего ссылок для скачивания: {search.num_links}")
            print(f"Успешно скачано: {success_downloads}")

        else:  # отказ от скачивания
            print(imaging_tools.line_separator)  # ---
            print("Скачки отменяются!")
            imaging_tools.bye_bye()

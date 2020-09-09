# -*- coding: utf-8 -*-
# main.py
# github.com/dimishpatriot/img_pars

from program import Program
# from searching import search_by_google
from searching import search_by_yandex
from tools import imaging_tools


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
        search = search_by_yandex.YandexSearch(path=program.path)

    if mach == 2:
        print("Поиск по Google пока не работает (см.выше). Запускаю Yandex :)\n")
        # search = search_by_google.GoogleSearch(program.path)
        search = search_by_yandex.YandexSearch(path=program.path)

    program.search_start(search)
    program.download_start(search)

    imaging_tools.bye_bye()  # прощание

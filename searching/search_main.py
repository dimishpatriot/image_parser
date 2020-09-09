# -*- coding: utf-8 -*-
# search_main.py
# github.com/dimishpatriot/img_pars

import os
from tools import imaging_tools


class Search:
    def __init__(self, program_path, maximum):
        print(" На какую тему изображения ты ищешь? ".center(80, '.'))
        self.text = input(">  ")
        search_folder = "_".join(self.text.split())
        self.results_path = os.path.join(program_path,
                                         f"search_result/{search_folder}")

    def get_quantity(self, maximum):
        print(f"Сколько тебе нужно? (максимально: {maximum})".center(80))
        while True:
            n_pict = input(">  ")
            if n_pict.isdigit():
                n_pict = int(n_pict)
                if n_pict <= maximum and n_pict > 0:
                    break
                elif n_pict == 0:
                    imaging_tools.bye_bye()
            print("Введи корректное значение!")
        return n_pict

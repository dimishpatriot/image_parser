# -*- coding: utf-8 -*-
# search_main.py
# github.com/dimishpatriot/img_pars

class Search:
    def __init__(self, path):
        self.path = path

    def q_search_text(self):
        print("Что ты ищешь?".center(80))
        self.text = input(">  ")

    def q_quantity(self, maximum):
        print(f"Сколько тебе нужно? (максимально: {maximum})".center(80))
        while True:
            n_pict = input(">  ")
            if n_pict.isdigit() and int(n_pict) <= maximum:
                break
            print("Введи корректное значение!")
        self.quantity = int(n_pict)

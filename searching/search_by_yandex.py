# -*- coding: utf-8 -*-
# search_by_yandex.py
# github.com/dimishpatriot/img_pars

from searching import search_main
from tools import html_tools
from tools import imaging_tools


class YandexSearch(search_main.Search):
    default_pics = 10
    maximum_pics = 100  # максимальная выдача без манипуляций ~100 картинок

    search_types = {"title": " Выбери тип поиска ",
                    1: f"Простой поиск. На выходе {default_pics} изображений",
                    2: "Расширенный поиск. Надо ввести количество и размер изображений",
                    3: "Комплексный поиск по количеству, размеру, типу, гамме, ориентации",
                    0: "Выход"}

    size_types = {"title": " Выбери нужный размер изображений ",
                  1: "large",
                  2: "medium",
                  3: "small"}

    gamma_types = {"title": " Выбери цветовую гамму ",
                   1: "color",
                   2: "grey",
                   3: "red",
                   4: "orange",
                   5: "yellow",
                   6: "cyan",
                   7: "green",
                   8: "blue",
                   9: "violet",
                   10: "white",
                   11: "black"}

    orient_types = {"title": " Выбери ориентацию изображений ",
                    1: "horizontal",
                    2: "vertical",
                    3: "square"}

    type_types = {"title": " Выбери нужный тип (формат файла) изображений ",
                  1: "photo",
                  2: "clipart",
                  3: "lineart",
                  4: "face",
                  5: "demotivator"}

    def __init__(self, path):
        super().__init__(program_path=path,
                         maximum=self.maximum_pics)
        self.size = None
        self.type = None
        self.gamma = None
        self.orientation = None
        self.search_type = imaging_tools.cons_menu(self.search_types)

        if self.search_type == 1:
            self.quantity = self.default_pics

        elif self.search_type == 2:
            self.quantity = self.get_quantity(self.maximum_pics)
            self.size = self.get_answer(self.size_types)

        elif self.search_type == 3:
            self.quantity = self.get_quantity(self.maximum_pics)
            self.size = self.get_answer(self.size_types)
            self.type = self.get_answer(self.type_types)
            self.gamma = self.get_answer(self.gamma_types)
            self.orientation = self.get_answer(self.orient_types)
        print("Запрос принят! Начинаю обработку...")

    def get_answer(self, types: dict) -> int:
        key = imaging_tools.cons_menu(types)
        output = types[key][1]
        return output

    def get_full_links(self, proxy, user_agent):
        search_string = "https://yandex.ru/images/search?text="

        if self.quantity > self.maximum_pics:
            self.numdoc = self.maximum_pics
        else:
            self.numdoc = self.quantity

        self.search_url = html_tools.transform_iri(search_string + self.text) + \
            self.get_size_str() + \
            self.get_orient_str() + \
            self.get_type_str() + \
            self.get_color_str() + \
            self.get_numdoc_str()
        print(f"Поисковый запрос сформирован > {self.search_url}")

        main_page_html = html_tools.get_html(self.search_url,
                                             proxy,
                                             user_agent)

        main_soup = html_tools.get_soup(main_page_html)
        print("+ soup is HOT :)")
        a_links = main_soup.find_all("a", class_="serp-item__link")
        print(imaging_tools.line_separator)
        return a_links

    def get_size_str(self):
        if self.size:  # формирование размера в строке запроса
            return "&isize=" + self.size
        else:
            return ""

    def get_orient_str(self):
        if self.orientation:  # формирование ориентации в строке запроса
            return "&iorient=" + self.orientation
        else:
            return ""

    def get_type_str(self):
        if self.type:  # формирование типа в строке запроса
            return "&type=" + self.type
        else:
            return ""

    def get_color_str(self):
        if self.gamma:  # формирование цвета в строке запроса
            return "&icolor=" + self.gamma
        else:
            return ""

    def get_numdoc_str(self):
        if self.numdoc:  # количества в строке запроса
            return "&numdoc=" + str(self.numdoc)
        else:
            return ""



from searching import search_main
from tools import html_tools
from tools import imaging_tools


class YandexSearch(search_main.Search):
    max_pix_1 = 15
    search_types = {0: 'Выбери тип поиска:',
                    1: 'Простой поиск. Надо ввести только поисковую строку. На выходе {} изображений'.format(max_pix_1),
                    2: 'Расширенный поиск. Надо ввести текст, количество и размер изображений',
                    3: 'Комплексный поиск. Вводится все (текст, количество, размер, тип, гамма, ориентация)'}
    size_types = {0: ('Выбери размер:', ''),
                  1: ('большой', 'large'),
                  2: ('средний', 'medium'),
                  3: ('малый', 'small')}
    gamma_types = {0: 'Выбери цветовую гамму:',
                   1: 'color',
                   2: 'grey',
                   3: 'red',
                   4: 'orange',
                   5: 'yellow',
                   6: 'cyan',
                   7: 'green',
                   8: 'blue',
                   9: 'violet',
                   10: 'white',
                   11: 'black'}
    orient_types = {0: 'Выбери ориентацию изображения:',
                    1: 'horizontal',
                    2: 'vertical',
                    3: 'square'}
    type_types = {0: 'Выбери тип изображения:',
                  1: 'photo',
                  2: 'clipart',
                  3: 'lineart',
                  4: 'face',
                  5: 'demotivator'}
    maximum_pics = 100

    def __init__(self, path):
        search_main.Search.__init__(self, path)

        self.size = None
        self.type = None
        self.gamma = None
        self.orientation = None

        self.search_type = imaging_tools.cons_menu(self.search_types)  # выбор типа поиска

        self.q_search_text()  # есть во всех вариантах

        if self.search_type == 1:
            self.quantity = 10

        elif self.search_type == 2:
            self.q_quantity(maximum=self.maximum_pics)
            self.size = self.get_answer(self.size_types)

        elif self.search_type == 3:
            self.q_quantity(maximum=self.maximum_pics)
            self.size = self.get_answer(self.size_types)
            self.type = self.get_answer(self.type_types)
            self.gamma = self.get_answer(self.gamma_types)
            self.orientation = self.get_answer(self.orient_types)

        print('Запрос принят! Начинаю обработку...')
        imaging_tools.split_line()

    def get_answer(self, types):
        key = imaging_tools.cons_menu(types, n=2)
        output = types[key][1]
        return output

    def html_yandex(self, proxy, user_agent):
        """
        поисковый механизм Яндекса
        максимальная выдача без манипуляций ~100 картинок
        """
        search_string = 'https://yandex.ru/images/search?text='  # поисковая строка
        max_num_page = 100  # количество изображений на страницу выдачи

        if self.quantity > max_num_page:
            numdoc = max_num_page
        else:
            numdoc = self.quantity

        self.search_url = html_tools.transform_iri(search_string + self.text) + \
                          self.get_size_str() + \
                          self.get_orient_str() + \
                          self.get_type_str() + \
                          self.get_color_str() + \
                          self.get_numdoc_str(numdoc)

        print('Поисковый запрос сформирован > ', self.search_url)

        main_page_html = html_tools.get_html(self.search_url, proxy, user_agent)  # чтение html

        main_soup = html_tools.get_soup(main_page_html)

        # print('+ soup is hot :)')

        a_links = main_soup.find_all(
            'a',
            class_='serp-item__link')

        imaging_tools.split_line()

        return a_links


    def get_size_str(self):
        if self.size is None:  # формирование размера в строке запроса
            st = ''
        else:
            st = '&isize=' + self.size
        return st

    def get_orient_str(self):
        if self.orientation is None:  # формирование ориентации в строке запроса
            st = ''
        else:
            st = '&iorient=' + self.orientation
        return st

    def get_type_str(self):
        if self.type is None:  # формирование типа в строке запроса
            st = ''
        else:
            st = '&type=' + self.type
        return st

    def get_color_str(self):
        if self.gamma is None:  # формирование цвета в строке запроса
            st = ''
        else:
            st = '&icolor=' + self.gamma
        return st

    def get_numdoc_str(self, numdoc):
        if numdoc is None:  # формирование цвета в строке запроса
            st = ''
        else:
            st = '&numdoc=' + str(numdoc)
        return st

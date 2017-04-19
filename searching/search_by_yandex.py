import urllib

from tools import html_tools

from searching import search_main
from tools import imaging_tools


class YandexSearch(search_main.Search):
    search_types = {0: 'Select type of search:',
                    1: 'Simple search. Only text string input. Output - 10 pics',
                    2: 'Extend search. Input text, quantity, size',
                    3: 'Complex search. Input all (text, quantity, size, type, etc...)'}
    size_types = {0: 'Select size:',
                  1: 'large',
                  2: 'medium',
                  3: 'small'}
    gamma_types = {0: 'Select main color gamma:',
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
    orient_types = {0: 'Select orientation:',
                    1: 'horizontal',
                    2: 'vertical',
                    3: 'square'}
    type_types = {0: 'Select type:',
                  1: 'photo',
                  2: 'clipart',
                  3: 'lineart',
                  4: 'face',
                  5: 'demotivator'}
    maximum_pics = 100

    def __init__(self, path):
        self.path = path
        self.size = None
        self.type = None
        self.gamma = None
        self.orientation = None
        self.machine = search_main.Search.search_machines[1]  # 1 - яндекс-поиск

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

    def get_answer(self, types):
        key = imaging_tools.cons_menu(types)
        output = types[key]
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

        print('search_url = ', self.search_url)

        main_page_html = html_tools.get_html(self.search_url, proxy, user_agent)  # чтение html

        main_soup = html_tools.get_soup(main_page_html)

        print('+ soup is hot :)')

        a_links = main_soup.find_all(
            'a',
            class_='serp-item__link')

        print('i have ({}) links:'.format(len(a_links)))
        urls = []

        f = open(self.path + \
                 '/search_result/' + \
                 '_'.join(self.text.split(' ')) + \
                 '/urls_list.txt',
                 'w')  # открытые файла на запись, имя - согласно запроса

        for a in a_links[:self.quantity]:
            s1 = a.attrs['href']  # находим атрибут с адресом
            if self.orientation:
                s2 = s1.split('&iorient=')[-2]  # отрезаем хвост (КОСТЫЛЬ!!!)
            else:
                s2 = s1.split('&pos=')[-2]  # отрезаем хвост (КОСТЫЛЬ!!!)

            s3 = s2.split('img_url=')[-1]  # отрезаем голову
            s4 = urllib.parse.unquote_plus(
                s3, encoding='utf-8')  # раскодируем

            print('url: ', s4)
            urls.append(s4)
            f.write(s4 + '\n')

        if len(urls) > 0:
            print('+ urls_list complete. len=', len(urls))
            print('+ urls_list save to /search_result/' + self.text + '/urls_list.txt')
        else:
            print('- url list is empty!')

        self.urls_list = urls

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

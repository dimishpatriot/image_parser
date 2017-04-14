import os
import urllib
import html_tools
import useragents_tools
import proxy_tools
import file_tools


class SM:
    search_machine = 'https://yandex.ru/images/search?text='
    max_num_page = 100  # количество изображений на страницу выдачи

    def __init__(self, search_text, num_pics, folder, search_size=None):
        self.search_text = search_text
        self.num = num_pics
        self.urls_list = []
        self.folder_to_save = os.getcwd() + folder  # полный путь
        self.search_size=search_size

        file_tools.make_dir(self.folder_to_save)  # проверяется и создается папка

    def search_links(self):
        if self.num > self.max_num_page:
            numdoc = self.max_num_page
        else:
            numdoc = self.num

        search_url=html_tools.get_search_url(
            search_machine=self.search_machine,
            search_text=self.search_text,
            numdoc=numdoc,
            size=self.search_size)

        print('search_url = ', search_url)

        proxy = proxy_tools.get_proxy()
        useragent = useragents_tools.get_useragent()
        main_page_html = html_tools.get_html(search_url, proxy, useragent)  # чтение html

        main_soup = html_tools.get_soup(main_page_html)

        print('+ soup is hot :)')

        a_links = main_soup.find_all(
            'a',
            class_='serp-item__link')

        print('i have ({}) links:'.format(len(a_links)))
        urls = []

        f = open(self.folder_to_save + 'urls_list.txt', 'w')

        for a in a_links[:self.num]:
            s1 = a.attrs['href']  # находим атрибут с адресом
            s2 = s1.split('&pos=')[-2]  # отрезаем хвост
            s3 = s2.split('img_url=')[-1]  # отрезаем голову
            s4 = urllib.parse.unquote_plus(
                s3, encoding='utf-8')  # раскодируем
            print('url: ', s4)
            urls.append(s4)
            f.write(s4 + '\n')

        if len(urls) > 0:
            print('+ urls_list complete. len=', len(urls))
            print('+ urls_list save to /search_result/' + self.search_text + '/urls_list.txt')
        else:
            print('- url list is empty!')

        self.urls_list = urls

import urllib
import html_tools
import useragents_tools
import proxy_tools
import iri_to_uri


class SM:
    search_machine = 'https://yandex.ru/images/search?text='
    max_num_page = 100  # количество изображений на страницу выдачи

    def __init__(self, search_text, num_pics):
        self.text = search_text
        self.num = num_pics
        self.urls_list=[]

    def search_links(self):
        if self.num > self.max_num_page:
            numdoc = self.max_num_page
        else:
            numdoc = self.num

        search_url = iri_to_uri.transform(self.search_machine + self.text) + '&numdoc=' + str(numdoc)
        print('search_url = ', search_url)

        proxy = proxy_tools.get_proxy()
        useragent = useragents_tools.get_useragent()
        main_page_html = html_tools.get_html(search_url, proxy, useragent)  # чтение html

        main_soup = html_tools.get_soup(main_page_html)

        print('+ soup is hat :)')

        a_links = main_soup.find_all('a', class_='serp-item__link')

        print('i have ({}) links:'.format(len(a_links)))
        urls = []
        for a in a_links[:self.num]:
            s1 = a.attrs['href']  # находим атрибут с адресом
            s2 = s1.split('&pos=')[-2]  # отрезаем хвост
            s3 = s2.split('img_url=')[-1]  # отрезаем голову
            s4 = urllib.parse.unquote_plus(
                s3, encoding='utf-8')  # раскодируем
            print('url: ', s4)
            urls.append(s4)

        if len(urls)>0:
            print('+ urls_list complete. len=: ', len(urls))
        else:
            print ('- url list is empty!')

        self.urls_list=urls
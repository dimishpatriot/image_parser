import urllib
from urllib.parse import quote, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup


def get_html(url, proxy, user_agent):
    """
    получение HTML
    :param url: искомый урл
    :param proxy: текущий прокси
    :param user_agent: текущий useragent
    :return: 
    """
    page_html = None
    try:
        print('Пробую получить html...')
        page_html = requests.get(
            url=url,
            headers=user_agent,
            proxies=proxy).text  # чтение html
        print('+ html получен!')

    except:
        print('- html не доступен в данный момент!')

    return page_html


def get_soup(html):
    """
    варим суп
    :param html: исходный сырой html
    """
    return BeautifulSoup(html, 'lxml')


def transform_iri(iri):
    """
    при необходимости преобразует кириллицу в URI
    """
    parts = urlsplit(iri)
    uri = urlunsplit((parts.scheme, parts.netloc.encode('idna').decode(
        'ascii'), quote(parts.path), quote(parts.query, '='), quote(parts.fragment),))

    return uri


def clear_links(obj, links):
    a_links = links
    print('Найдено ({}) ссылок на изображения:'.format(len(a_links)))
    urls = []

    f = open(obj.path + \
             '/search_result/' + \
             '_'.join(obj.text.split(' ')) + \
             '/urls_list.txt',
             'w')  # открытые файла на запись, имя - согласно запроса

    for a in a_links[:obj.quantity]:
        s1 = a.attrs['href']  # находим атрибут с адресом
        if obj.orientation:
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
        print('+ Лист ссылок сформирован. Количество: ', len(urls), ' шт.')
        print('+ Лист ссылок записан в файл > /search_result/' + obj.text + '/urls_list.txt')
    else:
        print('- Лист ссылок пуст!')

    obj.urls_list = urls

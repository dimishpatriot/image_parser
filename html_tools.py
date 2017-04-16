import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, urlsplit, urlunsplit


def get_html(url, proxy, user_agent):
    page_html = None
    try:
        print('try to get html....')
        page_html = requests.get(
            url=url,
            headers=user_agent,
            proxies=proxy).text  # чтение html
        print('+ get html - OK')

    except:
        print('- html not available')

    return page_html


def get_soup(html):
    return BeautifulSoup(html, 'lxml')


def get_search_url(search_machine, search_text, numdoc, size=None, orient=None, type=None, color=None):

    url = transform_iri(search_machine + search_text) + \
          get_size_str(size) + \
          get_orient_str(orient) + \
          get_type_str(type) + \
          get_color_str(color) + \
          get_numdoc_str(numdoc)

    return url


def transform_iri(iri):  # при необходимости преобразует кириллицу в URI
    parts = urlsplit(iri)
    uri = urlunsplit((parts.scheme, parts.netloc.encode('idna').decode(
        'ascii'), quote(parts.path), quote(parts.query, '='), quote(parts.fragment),))

    return uri


def get_size_str(size):
    if size is None:  # формирование размера в строке запроса
        st = ''
    else:
        st = '&isize=' + size
    return st


def get_orient_str(orient):
    if orient is None:  # формирование ориентации в строке запроса
        st = ''
    else:
        st = '&iorient=' + orient
    return st


def get_type_str(type):
    if type is None:  # формирование типа в строке запроса
        st = ''
    else:
        st = '&type=' + type
    return st


def get_color_str(color):
    if color is None:  # формирование цвета в строке запроса
        st = ''
    else:
        st = '&icolor=' + color
    return st


def get_numdoc_str(numdoc):
    if numdoc is None:  # формирование цвета в строке запроса
        st = ''
    else:
        st = '&numdoc=' + str(numdoc)
    return st

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, urlsplit, urlunsplit


def get_html(url, proxy, user_agent):
    page_html = None
    try:
        print('try to get html....')
        page_html = requests.get(
            url, headers=user_agent, proxies=proxy).text  # чтение html
        print('+ get html - OK')
    except:
        print('- html not available')

    return page_html


def get_soup(html):
    return BeautifulSoup(html, 'lxml')


def transform(iri):  # преобразует кириллицу в URI
    parts = urlsplit(iri)
    uri = urlunsplit((parts.scheme, parts.netloc.encode('idna').decode(
        'ascii'), quote(parts.path), quote(parts.query, '='), quote(parts.fragment),))
    return uri

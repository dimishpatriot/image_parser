import requests
from bs4 import BeautifulSoup


def get_html(url, proxy, useragent):

    try:
        print('try to get html....')
        page_html = requests.get(
            url, headers=useragent, proxies=proxy).text  # чтение html
        print('+ html - OK')

    except:
        page_html = None

    # print(page_html)

    return page_html


def get_soup(html):
    return BeautifulSoup(html, 'lxml')
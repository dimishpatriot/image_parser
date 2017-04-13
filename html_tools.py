import requests
from bs4 import BeautifulSoup


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

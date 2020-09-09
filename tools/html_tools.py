# -*- coding: utf-8 -*-
# html_tools.py
# github.com/dimishpatriot/img_pars

import urllib
from urllib.parse import quote, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup
from tools import check_tools


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
        print("Пробую получить html...")
        page_html = requests.get(
            url=url,
            headers=user_agent,
            proxies=proxy).text  # чтение html
        print("+ html получен!")

    except:
        print("- html не доступен в данный момент!")

    return page_html


def get_soup(html):
    """
    варим суп
    :param html: исходный сырой html
    """
    return BeautifulSoup(html, "lxml")


def transform_iri(iri):
    """
    при необходимости преобразует кириллицу в URI
    """
    parts = urlsplit(iri)
    uri = urlunsplit((parts.scheme,
                      parts.netloc.encode("idna").decode("ascii"),
                      quote(parts.path),
                      quote(parts.query, "="),
                      quote(parts.fragment),))
    return uri


def clear_links(obj) -> list:
    urls = []
    print("Найдены ссылки на изображения:")
    # открытые файла на запись, имя - согласно запроса
    with open(f"{obj.path}/search_result/{obj.text}/urls_list.txt", "w") as f:
        for a in obj.links[:obj.quantity]:
            addr = a.attrs["href"].split("&img_url=")[1].split("&text=")[0]
            if "&isize=" in addr:
                addr = addr.split("&isize=")[0]
            if "&iorient=" in addr:
                addr = addr.split("&iorient=")[0]

            url = urllib.parse.unquote_plus(addr, encoding="utf-8")
            if check_tools.link_is_pic(url):
                urls.append(url)
                f.write(url + "\n")
                print("url: ", url)

    if len(urls) > 0:
        print(f"+ Лист ссылок сформирован. Количество: {len(urls)} шт.")
        print(f"+ Лист ссылок записан в файл > /search_result/{obj.text}/urls_list.txt")
    else:
        print("- Лист ссылок пуст!")

    return urls

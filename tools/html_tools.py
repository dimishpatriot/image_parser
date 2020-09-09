# -*- coding: utf-8 -*-
# html_tools.py
# github.com/dimishpatriot/img_pars

import urllib
from urllib.parse import quote, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup
from tools import check_tools, imaging_tools


def get_html(url, proxy, user_agent):
    page_html = None
    try:
        print("Пробую получить html...")
        page_html = requests.get(
            url=url,
            headers=user_agent,
            proxies=proxy).text  # чтение html
        print("+ html получен!")

    except:
        print("- html не доступен в данный момент! пробуй еще")
        imaging_tools.bye_bye()

    return page_html


def get_soup(html):
    return BeautifulSoup(html, "lxml")


def transform_iri(iri):
    parts = urlsplit(iri)
    # при необходимости преобразует кириллицу в URI
    uri = urlunsplit((parts.scheme,
                      parts.netloc.encode("idna").decode("ascii"),
                      quote(parts.path),
                      quote(parts.query, "="),
                      quote(parts.fragment),))
    return uri


def clear_links(raw_links) -> list:
    urls = []
    if len(raw_links) > 0:
        print("Найдены ссылки на изображения:")
        for a in raw_links:
            addr = a.attrs["href"].split("&img_url=")[1].split("&text=")[0]
            if "&isize=" in addr:
                addr = addr.split("&isize=")[0]
            if "&iorient=" in addr:
                addr = addr.split("&iorient=")[0]

            url = urllib.parse.unquote_plus(addr,
                                            encoding="utf-8")
            if check_tools.link_is_pic(url):
                urls.append(url)
                print("url: ", url)

    return urls

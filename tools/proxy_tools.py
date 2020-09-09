# -*- coding: utf-8 -*-
# proxy_tools.py
# github.com/dimishpatriot/img_pars

from random import choice
from tools import html_tools
from tools import useragents_tools


def proxy_update(proxy: str, main_path: str) -> None:
    print("Пробую обновить лист прокси...")
    useragent = useragents_tools.get_useragent(main_path)

    new_ip = []
    url = "https://hidemy.name/ru/proxy-list/?ports=80&type=h&anon=34#list"
    # сайт с текущими доступными проксями
    html = html_tools.get_html(url, proxy, useragent)
    soup = html_tools.get_soup(html)
    ip_list = soup.find_all("td", class_="tdl")

    for i in ip_list:
        new_ip.append(i.text + ":80")

    if new_ip:
        save_proxy_list(new_ip, main_path)
        print("+ прокси-лист успешно обновлен")
    else:
        print(
            "- что-то пошло не так, прокси-лист будет старый, но, возможно, вполне рабочий")


def get_proxy(path: str) -> dict:
    print("Пробую сменить прокси...")
    px_list = open(path + "/lists/proxy_list.txt").read().splitlines()
    proxy = {"http": "http://" + choice(px_list)}
    print(f"+ прокси успешно подменен: {proxy}")
    proxy_update(proxy, path)
    return proxy


def save_proxy_list(new_proxy_list: list, path: str) -> None:
    with open(path + "/lists/proxy_list.txt", "w") as f:
        for x in new_proxy_list:
            f.write(x + "\n")

from random import choice

import html_tools
import imaging_tools
import useragents_tools


def proxy_update(proxy):
    """
    обновление листа прокси
    :param proxy: старый прокси
    """
    print('try to update px-list....')

    useragent = useragents_tools.get_useragent()

    new_ip = []
    url = 'https://hidemy.name/ru/proxy-list/?ports=80&type=h&anon=34#list'
    # сайт с текущими доступными проксями
    html = html_tools.get_html(url, proxy, useragent)
    soup = html_tools.get_soup(html)

    ip_list = soup.find_all('td', class_='tdl')

    for i in ip_list:
        new_ip.append(i.text + ':80')

    if new_ip:
        save_proxy_list(new_ip)
        print('+ proxy list update - OK')
    else:
        print('- proxy list will old eat')

    imaging_tools.split_line()  # ---


def get_proxy():
    """
    получение прокси из proxy_list.txt
    :return: новый прокси
    """
    px_list = open('proxy_list.txt').read().split('\n')

    proxy = {'http': 'http://' + choice(px_list)}
    print('+ make fake proxy - OK: ', proxy)
    proxy_update(proxy)

    return proxy


def save_proxy_list(new_proxy_list):
    """
    обновление/запись proxy_list.txt
    :param new_proxy_list: 
    :return: 
    """
    f = open('proxy_list.txt', 'w')
    for x in new_proxy_list:
        f.write(x+'\n')
    f.close()

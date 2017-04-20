from random import choice

from tools import html_tools
from tools import useragents_tools


def proxy_update(proxy, main_path):
    """
    обновление листа прокси
    :param main_path: путь главной папки
    :param proxy: старый прокси
    """
    print('Пробую обновить лист прокси...')

    useragent = useragents_tools.get_useragent(main_path)

    new_ip = []
    url = 'https://hidemy.name/ru/proxy-list/?ports=80&type=h&anon=34#list'
    # сайт с текущими доступными проксями
    html = html_tools.get_html(url, proxy, useragent)
    soup = html_tools.get_soup(html)

    ip_list = soup.find_all('td', class_='tdl')

    for i in ip_list:
        new_ip.append(i.text + ':80')

    if new_ip:
        save_proxy_list(new_ip, main_path)
        print('+ прокси-лист успешно обновлен')
    else:
        print('- что-то пошло не так, прокси-лист будет старый, но, возможно, вполне рабочий')


def get_proxy(path):
    """
    получение прокси из proxy_list.txt
    :return: новый прокси
    """
    px_list = open(path+'/lists/proxy_list.txt').read().split('\n')

    proxy = {'http': 'http://' + choice(px_list)}
    print('+ прокси успешно подменен: ', proxy)
    proxy_update(proxy, path)

    return proxy


def save_proxy_list(new_proxy_list, path):
    """
    обновление/запись proxy_list.txt
    :param path:  путь главной папки
    :param new_proxy_list: 
    """
    f = open(path+'/lists/proxy_list.txt', 'w')
    for x in new_proxy_list:
        f.write(x+'\n')
    f.close()

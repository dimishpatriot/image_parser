from random import choice
import useragents_tools
import html_tools


def proxy_update(proxy):
    print('try to update px-list....')

    useragent = useragents_tools.get_useragent()

    new_ip = []
    url = 'https://hidemy.name/ru/proxy-list/?ports=80&type=h&anon=34#list'
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


def get_proxy():
    px_list = open('proxy_list.txt').read().split('\n')

    proxy = {'http': 'http://' + choice(px_list)}
    print('+ make fake proxy - OK: ', proxy)
    proxy_update(proxy)

    return proxy


def save_proxy_list(new_proxy_list):
    f = open('proxy_list.txt', 'w')
    for x in new_proxy_list:
        f.write(x+'\n')
    f.close()

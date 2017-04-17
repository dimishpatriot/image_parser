from random import choice

import imaging_tools


def get_useragent():
    """
    получение случайного Useragent из файла
    :return: 
    """
    try:
        ua_list = open('useragents_list.txt').read().split('\n')

        useragent = {'User-Agent': choice(ua_list)}
        print('+ user-agent select - OK', useragent)
    except:
        useragent = None
        print('- you have not user-agent yet')

    imaging_tools.split_line()  # ---

    return useragent

from random import choice

from tools import imaging_tools


def get_useragent(path):
    """
    получение случайного Useragent из файла
    :return: 
    """
    try:
        ua_list = open(path+'/lists/useragents_list.txt').read().split('\n')

        user_agent = {'User-Agent': choice(ua_list)}
        print('+ user-agent select - OK', user_agent)
    except:
        user_agent = None
        print('- you have not user-agent yet')

    imaging_tools.split_line()  # ---

    return user_agent

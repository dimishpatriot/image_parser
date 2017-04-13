from random import choice


def get_useragent():
    try:
        ua_list = open('useragents_list.txt').read().split('\n')

        useragent = {'User-Agent': choice(ua_list)}
        print('+ user-agent select - OK', useragent)
    except:
        useragent = None
        print('- you have not user-agent yet')
    return useragent

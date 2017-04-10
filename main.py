import imaging  # красоты там :)
import machine_search  # поисковая машина
import machine_download  # машина для закачки

# START


if __name__ == '__main__':
    ver = '0.1'
    rep = 'https://github.com/dimishpatriot/img_pars.git'
    imaging.welcome(version=ver, repository=rep)

    text = input('what do you search? ')
    num = int(input('how match pics you need? '))

    my_s = machine_search.SM(search_text=text, num_pics=num)
    my_s.search_links()

    if len(my_s.urls_list) > 0:
        folder_to_save = '/search_result/' + '_'.join(text.split(' ')) + '/'
        my_d = machine_download.DM(url_list=my_s.urls_list, folder=folder_to_save)
        my_d.downloader()

    imaging.byebye()

import os
import requests
import file_tools
import test_tools
import download_multiplicator
import imaging_tools


class DM:
    def __init__(self, folder, search_text, multi_dwn):
        self.folder_to_save = os.getcwd() + folder  # полный путь
        self.url_list = open(self.folder_to_save + '/urls_list.txt')
        self.text = search_text

        file_tools.make_dir(self.folder_to_save)  # проверяется и создается папка
        print('+ your folder is \'{}\''.format(self.folder_to_save))

        if multi_dwn:
            success_links, all_links = self.multi_way()

        else:
            success_links, all_links = self.one_way()

        imaging_tools.split_line()  # ---

        print('all links: ', all_links)
        print('success links: ', success_links)

        imaging_tools.split_line()  # ---

    def one_way(self):
        success = 0
        n = 1

        for u in self.url_list:
            file_name, url = file_tools.get_file_name(u, n, text=self.text)
            if test_tools.link_is_pic(url):
                print('file #{0} \'{1}\' now downloading'.format(n, file_name))
                n += 1

                try:
                    r = requests.get(url, stream=True)
                    if r.status_code == 200:
                        with open(self.folder_to_save + '/' + file_name, 'bw') as f:
                            for chunk in r.iter_content(102400):
                                f.write(chunk)
                        success += 1

                        print('- OK')
                    else:
                        print('- not available now')
                except:
                    print('- false!')
            else:
                print('-link is not picture!')
                n += 1
                continue

        return success, n  # возвращает число успешных исходов и общее число исходов (строк в файле)

    def multi_way(self):
        success = 0  # TODO реализовать подсчет успешных исходов
        n = 0
        dwn = []

        for u in self.url_list:
            file_name, url = file_tools.get_file_name(u, n, text=self.text)

            if test_tools.link_is_pic(url):
                dwn.append(download_multiplicator.MD(url, file_name, self.folder_to_save))
                dwn[n].start()
                n += 1
            else:
                print('- link is not picture!')
                continue

        for x in range(n):
            dwn[x].join()  # завершение потоков

        return success, n

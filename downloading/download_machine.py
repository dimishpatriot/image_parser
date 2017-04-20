import requests

from downloading import download_multiplicator
from tools import file_tools, check_tools


class DM:
    def __init__(self, obj):
        self.folder_to_save = file_tools.get_result_folder_name(obj)  # полный путь
        self.url_list = open((self.folder_to_save + 'urls_list.txt'), 'r')  # список ссылок для скачивнаия

        self.text = obj.text

        file_tools.make_dir(self.folder_to_save)  # проверяется и создается папка
        print('+ твоя папка для сохранений \'{}\''.format(self.folder_to_save))

    def one_way(self):
        """
        однопоточная закачка
        """
        print()
        print('Однопоточное скачивание (для терпеливых)...')
        success = 0
        n_string = 1

        for u in self.url_list:
            file_name, url = file_tools.get_file_name(u, n_string, text=self.text)
            print('файл #{0} \'{1}\' сейчас скачивается'.format(n_string, file_name))
            n_string += 1

            try:
                r = requests.get(url, stream=True)
                if r.status_code == 200:
                    with open(self.folder_to_save + '/' + file_name, 'bw') as f:
                        for chunk in r.iter_content(102400):
                            f.write(chunk)
                    success += 1
                    print('- OK')
                else:
                    print('- не доступен')
            except:
                print('- ошибка!')

        self.all_links = n_string
        self.success_links = success

    def multi_way(self):
        """
        мультипоточная закачка
        :return: успешность, количество строк
        """
        print()
        print('Многопоточное скачивание...')
        success = 0
        n_process_start = 0
        n_string = 0
        dwn = []

        for u in self.url_list:
            n_string += 1
            url = u.rstrip()  # удаление символа конца строки в строке файла
            file_name = file_tools.get_file_name(url, n_process_start, text=self.text)

            if check_tools.link_is_pic(url):
                dwn.append(download_multiplicator.MD(url, file_name, self.folder_to_save))
                dwn[n_process_start].start()
                n_process_start += 1
            else:
                continue

        for x in range(n_process_start):  # остановка только запущенных потоков
            dwn[x].join()
            success += dwn[x].success_flag  # завершение потоков

        self.all_links = n_string
        self.success_links = success

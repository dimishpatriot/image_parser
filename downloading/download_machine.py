# -*- coding: utf-8 -*-
# download_machine.py
# github.com/dimishpatriot/img_pars

import requests
from downloading import download_multiplicator
from tools import file_tools, check_tools


class DM:
    def __init__(self, path: str, search_text: str):
        self.folder_to_save = path
        self.search_text = "".join(search_text.split())
        print(f"+ твоя папка для сохранений: {self.folder_to_save}")

    def one_way(self, urls_list: list) -> None:
        print("\nОднопоточное скачивание (для терпеливых)...")
        success = 0
        counter = 1

        for u in urls_list:
            url = u.rstrip()  # удаление символа конца строки в строке файла
            file_name = file_tools.get_file_name(url,
                                                 counter,
                                                 text=self.search_text)
            print(f"файл #{counter:<4} сейчас скачивается")
            counter += 1

            try:
                r = requests.get(url, stream=True)
                if r.status_code == 200:
                    with open(f"{self.folder_to_save}/{file_name}", "bw") as f:
                        for chunk in r.iter_content(102400):
                            f.write(chunk)
                    success += 1
                    print("- OK")
                else:
                    print("- не доступен")
            except:
                print("- ошибка!")
        return success

    def multi_way(self, urls_list: list) -> None:
        print("\nМногопоточное скачивание...")
        success = 0
        n_process_start = 0
        dwn = []

        for u in urls_list:
            url = u.rstrip()
            file_name = file_tools.get_file_name(url,
                                                 n_process_start,
                                                 text=self.search_text)

            if check_tools.link_is_pic(url):
                dwn.append(download_multiplicator.MD(url,
                                                     file_name,
                                                     self.folder_to_save))
                dwn[n_process_start].start()
                n_process_start += 1
            else:
                continue

        for x in range(n_process_start):  # остановка только запущенных потоков
            dwn[x].join()
            success += dwn[x].success_flag  # завершение потоков
        return success

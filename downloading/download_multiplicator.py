# -*- coding: utf-8 -*-
# download_multiplicator.py
# github.com/dimishpatriot/img_pars

from threading import Thread
import requests


class MD(Thread):
    def __init__(self, url: str, file: str, folder: str):
        Thread.__init__(self)
        self.url = url
        self.file = file
        self.folder = folder
        self.success_flag = 0

    def run(self):
        max_attempt = 3  # максимально ечисло попытко
        attempt = 1  # счетчик попыток

        while attempt <= max_attempt:
            try:
                # получение реквеста, если неудачно, счетчик +1 и повтор
                r = requests.get(self.url, stream=True)

                if r.status_code in range(200, 300):  # проверка запроса на код 200
                    print(f"# {self.file} начал скачиваться...")

                    with open(self.folder + "/" + self.file, "bw") as f:
                        for chunk in r.iter_content(102400):
                            f.write(chunk)
                        self.success_flag = 1  # успешное скачивание
                    print(f"{self.file} - OK")
                    break
                elif r.status_code in range(500, 600):  # возможная ошибка сервера
                    print(self.file + " ответ сервера:",
                          r.status_code, "попытка: ", attempt)
                    attempt += 1
                else:  # прочие ошибки
                    print(f"{self.file} - ответ сервера: {r.status_code}")
                    break
            except:
                attempt += 1

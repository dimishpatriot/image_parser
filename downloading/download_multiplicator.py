from threading import Thread

import requests


class MD(Thread):
    """
    класс запуска многопоточного скачивания
    """

    def __init__(self, url, file, folder):
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
                r = requests.get(self.url, stream=True)  # получение реквеста, если неудачно, счетчик +1 и повтор

                if r.status_code == 200:  # проверка запроса на код 200
                    print('файл #{0} начал скачиваться...'.format(self.file))

                    with open(self.folder + '/' + self.file, 'bw') as f:

                        for chunk in r.iter_content(102400):
                            f.write(chunk)

                        self.success_flag = 1  # успешное скачивание
                    print(self.file + ' - OK')
                    break

                else:
                    print(self.file + ' ответ сервера:', r.status_code, 'попытка: ', attempt)
                    attempt += 1
            except:
                attempt += 1

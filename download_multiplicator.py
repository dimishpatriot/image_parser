from threading import Thread
import requests


class MD(Thread):
    def __init__(self, url, file, folder):
        Thread.__init__(self)
        self.url = url
        self.file = file
        self.folder = folder
        self.success_flag = 0

    def run(self):
        max_attempt = 3
        attempt = 1
        while attempt <= max_attempt:
            try:
                r = requests.get(self.url, stream=True)

                if r.status_code == 200:
                    print('file #{0} start downloading...'.format(self.file))
                    with open(self.folder + '/' + self.file, 'bw') as f:
                        for chunk in r.iter_content(10240):
                            f.write(chunk)
                        self.success_flag = 1
                    print(self.file + ' - OK')
                    attempt = max_attempt + 1

                else:
                    print(self.file + ' SK=', r.status_code, 'try=', attempt)
                    attempt += 1
            except:
                attempt += 1

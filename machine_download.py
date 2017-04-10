import os
import requests


class DM:
    def __init__(self, url_list, folder):
        self.url_list = url_list

        self.folder = os.getcwd() + folder  # полный путь

        if not os.path.exists(self.folder):  # проверка на наличие
            os.makedirs(self.folder)

        print('+ your folder is \'{}\''.format(self.folder))

    def downloader(self):  # dwn pictures to ..?
        success = 0
        for url in self.url_list:
            n = self.url_list.index(url) + 1
            pic_name = 'pic_' + str(n)

            file_ext = url.split('.')[-1]

            file_name = pic_name + '.' + file_ext

            print('file #{0} \'{1}\' now downloading'.format(n, file_name))

            try:

                r = requests.get(url, stream=True)
                if r.status_code == 200:
                    with open(self.folder + file_name, 'bw') as f:
                        for chunk in r.iter_content(102400):
                            f.write(chunk)
                    success += 1
                    print('- OK')
                else:
                    print('- not available now')
            except:
                print('- false!')

        print('all links: ', len(self.url_list))
        print('success download: ', success)

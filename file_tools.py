import os


def get_file_name(url, num, text):
    new_url = url.rstrip()  # убрать символ окончания строки
    pic_name = text + '_' + str(num).zfill(2)
    file_ext = new_url.split('.')[-1]
    file_name = pic_name + '.' + file_ext

    return file_name, new_url


def make_dir(folder):
    if not os.path.exists(folder):  # проверка на наличие папки
        os.makedirs(folder)


def folder_to_save(search_text):
    folder = '/search_result/' + '_'.join(search_text.split(' ')) + '/'  # имя папки для сохранения

    return folder

# -*- coding: utf-8 -*-
# main.py
# github.com/dimishpatriot/img_pars

import os


def get_file_name(url, num, text):
    """
    получение имени для сохраняемого файла изображения
    :param url: ссылка
    :param num: номер
    :param text: текст запроса
    :return: имя файла
    """
    pic_name = text + '_' + \
        str(num).zfill(2)  # полное имя из запроса и порядкового номера формата XX
    file_ext = url.split('.')[-1]  # определение расширения файла

    return pic_name + '.' + file_ext


def make_dir(folder):
    """
    создание рабочей директории для сохранения результатов
    :param folder: папка
    """
    if not os.path.exists(folder):  # проверка на наличие папки
        os.makedirs(folder)  # создание папки
        pass


def get_result_folder_name(obj):
    """
    получение имени папки с учетом текущего местоположения
    :return: имя папки
    """
    return obj.path + '/search_result/' + '_'.join(obj.text.split(' ')) + '/'  # имя папки для сохранения

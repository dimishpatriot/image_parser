# -*- coding: utf-8 -*-
# main.py
# github.com/dimishpatriot/img_pars

import os


def get_file_name(url: str, num: int, text: str) -> str:
    """
    получение имени для сохраняемого файла изображения
    :param url: ссылка
    :param num: номер
    :param text: текст запроса
    :return: имя файла
    """
    pic_name = f"{text}_{str(num).zfill(2)}"  # полное имя из запроса и порядкового номера формата XX
    file_ext = url.split(".")[-1]  # определение расширения файла
    return f"{pic_name}.{file_ext}"


def make_dir(folder: str) -> None:
    """
    создание рабочей директории для сохранения результатов
    :param folder: папка
    """
    if not os.path.exists(folder):  # проверка на наличие папки
        os.makedirs(folder)  # создание папки


def get_result_folder_name(obj) -> str:
    """
    получение имени папки с учетом текущего местоположения
    :return: имя папки
    """
    folder_name = "_".join(obj.text.split())
    return f"{obj.path}/search_result/{folder_name}/"  # имя папки для сохранения

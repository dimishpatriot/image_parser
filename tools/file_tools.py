# -*- coding: utf-8 -*-
# main.py
# github.com/dimishpatriot/img_pars

def get_file_name(url: str, num: int, text: str) -> str:
    pic_name = f"{text}_{str(num).zfill(2)}"  # полное имя из запроса и порядкового номера формата XX
    file_ext = url.split(".")[-1]  # определение расширения файла
    return f"{pic_name}.{file_ext}"


def save_links_to_file(clear_urls: list, path: str) -> None:
    with open(f"{path}/urls_list.txt", "w") as f:
        f.writelines(clear_urls)

# -*- coding: utf-8 -*-
# check_tools.py
# github.com/dimishpatriot/img_pars

def yes_or_no(answer: str) -> bool:
    d = ("y", "Y", "yes", "Yes", "YES", "ДА", "да", "Д", "д", "Да", "1")
    if answer in d:
        return True
    else:
        return False


def link_is_pic(url: str) -> bool:
    pic_ext = ("jpg", "jpeg", "png", "tiff", "bmp",
               "gif", "pcx", "epf", "ico", "cdr",
               "svg")
    ext = url.split(".")[-1]
    if ext in pic_ext:
        return True
    else:
        return False

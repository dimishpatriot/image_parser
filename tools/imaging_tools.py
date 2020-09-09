# -*- coding: utf-8 -*-
# imaging_tools.py
# github.com/dimishpatriot/img_pars

line_separator = "-" * 80


def welcome(program) -> None:
    print(line_separator)
    print(f"{program.name}__, версия {program.version}".center(80))
    print(f"{program.rep}".center(80))
    print(line_separator)
    print()


def bye_bye() -> None:
    print("Всех благ! Ты заходи, если что ^)")
    print(line_separator)
    exit()


def cons_menu(variant_dict: dict) -> int:
    for key in list(variant_dict.keys()):
        if key == "title":
            print(variant_dict[key][0:].center(80, '.'))  # вопрос
        else:
            print(f"{key:<2} {variant_dict[key][0:]}")  # варианты ответа

    while True:  # бесконечный цикл до выбора корректного ответа
        i = input("\n>  ")
        if i.isdigit():
            ans = int(i)
            if ans == 0:
                bye_bye()
            if ans in variant_dict.keys() and ans != "title":
                break
        print("Выбирай с умом!")
    return ans

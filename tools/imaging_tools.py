# -*- coding: utf-8 -*-
# imaging_tools.py
# github.com/dimishpatriot/img_pars

line_separator = "-" * 80


def welcome(program) -> None:
    """
    вступление
    :param program: выходные данные программы
    """
    print(line_separator)
    print(f"Велкам в  __{program.name}__, версия {program.version}")
    print(f"Автор: {program.author}")
    print(f"Хранилище: {program.rep}")
    print(line_separator)


def bye_bye() -> None:
    """
    прощальное слово
    """
    print("Всех благ! Ты заходи, если что ^)")
    print(line_separator)
    exit()


def cons_menu(variant_dict: dict) -> int:
    """
    выводит меню на экран и предоставляет выбор
    :param variant_dict:
    :param n: количество подвариантов в словаре
    :return:
    """
    for key in list(variant_dict.keys()):
        if key == "title":
            print(f"{variant_dict[key][0:]:^80}")  # вопрос
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
    print(line_separator)
    return ans

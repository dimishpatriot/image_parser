def welcome(program_data):
    """
    вступление
    :param program_data: выходные данные программы
    """
    print('=' * 78)
    print('Велкам в  __{0}__, версия {1}'.format(program_data.name, program_data.version))
    print('Автор: {}'.format(program_data.author))
    print('Хранилище: {}'.format(program_data.rep))
    print('=' * 78)


def bye_bye():
    """
    прощальное слово
    """
    print('Всех благ! Ты заходи, если что ^)')
    print('=' * 78)


def split_line():
    """
    разделительная линия
    """
    print('-' * 78)


def cons_menu(variant_dict, n=1):
    '''
    выводит меню на экран и предоставляет выбор
    :param variant_dict: 
    :param n: количество подвариантов в словаре
    :return: 
    '''
    if n == 1:
        for key in list(variant_dict.keys()):
            if key == 0:
                print(variant_dict[key])  # вопрос
            else:
                print(key, ' ', variant_dict[key])  # варианты ответа

    elif n == 2:
        for key in list(variant_dict.keys()):
            if key == 0:
                print(variant_dict[key][0])  # вопрос
            else:
                print(key, ' ', variant_dict[key][0])  # варианты ответа

    while True:
        try:
            ans = int(input('#: '))
            if ans in variant_dict.keys():
                ans_num = ans
                break
        except:
            pass

        print('Выбирай с умом!')

    split_line()  # ---

    return ans_num

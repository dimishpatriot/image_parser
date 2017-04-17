def welcome(program_data):
    """
    вступление
    :param program_data: выходные данные программы
    """
    print('=' * 78)
    print('Welcome to __{0}__, version {1}'.format(program_data.name, program_data.version))
    print('Author: {}'.format(program_data.author))
    print('Repository: {}'.format(program_data.rep))
    print('=' * 78)


def bye_bye():
    """
    прощальное слово
    """
    print('Bye Bye! See you later ^)')
    print('=' * 78)


def split_line():
    """
    разделительная линия
    """
    print('-' * 78)


def cons_menu(variant_dict):
    for key in list(variant_dict.keys()):
        if key == 0:
            print(variant_dict[key])  # вопрос
        else:
            print(key, ' ', variant_dict[key])  # варианты ответа

    while True:
        try:
            ans = int(input('#: '))
            if ans in variant_dict.keys():
                ans_num = ans
                break
        except:
            pass

        print('Make your right choice!')

    split_line()  # ---

    return ans_num

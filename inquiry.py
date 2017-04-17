import check_tools
import imaging_tools


class Search:
    search_machines = {0: 'Select search machine:',
                       1: 'Yandex.ru',
                       2: 'Google.com (not realised yet :)'}


    def __init__(self):
        self.text=None
        self.quantity=None

        self.machine_num = self.cons_menu(self.search_machines)  # выбор поискового механизма


    def cons_menu(self, variant_dict):
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

        imaging_tools.split_line()  # ---

        return ans_num

    def q_search_text(self):
        print('Write, what you are looking for')
        self.text = input('# ')

    def q_quantity(self, maximum):
        print('How many images do you need (max: {})'.format(maximum))
        while True:
            n_pict = input('# ')

            if not check_tools.is_num(n_pict, max_value=maximum):
                print('Input correct value!')
            else:
                break
        self.quantity = int(n_pict)

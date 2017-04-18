from tools import imaging_tools, check_tools


class Search:
    search_machines = {0: 'Select search machine:',
                       1: 'Yandex.ru',
                       2: 'Google.com (not realised yet :)'}

    def __init__(self, program):
        self.machine_num = imaging_tools.cons_menu(self.search_machines)  # выбор поискового механизма
        self.path = program.path

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

import check
import imaging_tools


class SearchObject:
    search_types = {0: 'Select type of search:',
                    1: 'Simple search. Only text string input. Output - 10 pics',
                    2: 'Extend search. Input text, quantity, size',
                    3: 'Complex search. Input all (text, quantity, size, type, gamma, orientation)'}

    size_types = {0: 'Select size:',
                  1:'large',
                  2:'medium',
                  3:'small'}

    gamma_types={0:'Select main color gamma:',
                   1:'color',
                   2:'grey',
                   3:'red',
                   4:'orange',
                   5:'yellow',
                   6:'cyan',
                   7:'green',
                   8:'blue',
                   9:'violet',
                   10:'white',
                   11:'black'}

    orient_types={0:'Select orientation:',
                  1:'horizontal',
                  2:'vertical',
                  3:'square'}

    type_types={0:'Select type:',
                1:'photo',
                2:'clipart',
                3:'lineart',
                4:'face',
                5:'demotivator'}

    def __init__(self):

        self.size = None
        self.type = None
        self.gamma = None
        self.orientation = None

        search_type=self.cons_menu(self.search_types)

        if check.is_num(search_type):
            search_type=int(search_type)

        if search_type == 1:
            self.text = self.q_search_text()
            self.quantity=10


        elif search_type == 2:
            self.text = self.q_search_text()
            self.quantity = self.q_quantity()
            self.size = self.get_answer(self.size_types)

        elif search_type == 3:
            self.text = self.q_search_text()
            self.quantity = self.q_quantity()
            self.size = self.get_answer(self.size_types)
            self.type = self.get_answer(self.type_types)
            self.gamma = self.get_answer(self.gamma_types)
            self.orientation = self.get_answer(self.orient_types)


    def q_search_text(self):
        print('Write, what you are looking for')
        st = input('# ')
        return st


    def q_quantity(self):
        print('How many images do you need (max: 100)')
        while True:
            n_pict = input('# ')

            if not check.is_num(n_pict):
                print('Input correct value!')
            else:
                break
        qt = int(n_pict)
        return qt

    def get_answer (self, types):
        key=self.cons_menu(types)
        output = types[key]
        return output



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
                    ans_num=ans
                    break
            except:
                pass

            print('Make your right choice!')

        imaging_tools.split_line()  # ---

        return ans_num

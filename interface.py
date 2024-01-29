# в этом файле реазилуется консольный интерфейс программы с питомникком

from nursery import *

nursery = Nursery()

class Interface:

    @staticmethod
    def menu():
        print('Добро пожаловать в питомник домашних животных!!!\nНиже представлен возможный функционал программы:')
        print('--------------------------------------------------------------------------------------------------')
        map_menu = {1: 'посмотреть информацию о питомнике',
                    2: 'посмотреть список всех питомцев',
                    3: 'добавить нового питомца',
                    4: 'обучить питомца новым навыкам',
                    5: 'просмотреть навыки питомца',
                    0: 'покинуть питомник'}
        ls_map_menu = list(map_menu.items())
        for item in ls_map_menu:
            print(f'{item[0]} ------------ {item[1]}')
        result = input("**********ВВЕДИТЕ ЦИФРУ НУЖНОГО ПУНКТА МЕНЮ***************\n:  ")
        return result
    
    @staticmethod
    def print_cat():
        print('''
                                                                        ╱▔▔╲▂▂▂╱▔▔╲
                                                                        ╲╱╳╱▔╲╱▔╲╱▔
                                                                        ┈┈┃▏▕▍▏▕▍▏
                                                                        ┈┈┃╲▂╱╲▂╱╲┈╭━╮
                                                                        ┈┈┃┊┳┊┊┊┊┊▔╰┳╯
                                                                        ┈┈┃┊╰━━━┳━━━╯
                                                                        ┈┈┃┊┊┊┊╭╯''')


    def run():


        flag = True
        while flag:
            flag = Interface.menu()
            flag = int(flag)
            if flag == 1:
                nursery.info()
                Interface.print_cat()
            elif flag == 2:
                Nursery.display_all_animals()
                Interface.print_cat()

        Interface.print_cat()
        print('\t\t\t\t\t\t\t\t\tДо встречи!!! Животным было с Вами очень интересно!!!')

Interface.run()




# в этом файле реазилуется консольный интерфейс программы с питомникком
from db_connector import *
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
            elif flag == 3:
                name = ''
                age = 0
                voice = ''
                while True:
                    name = input('                              введите имя питомца: ')
                    try:
                        if name:
                            break
                    except Exception:
                        print('Питомец без клички не бывает!!!!')
                        continue
                while True:
                    age = input('                              введите возраст питомца: ')
                    try:
                        if int(age) > 0 and int(age) < 50:
                            break
                    except Exception:
                        print('Недопустимый возраст питомца!!!!')
                        continue
                while True:
                    voice = input('                              какие звуки издает Ваш питомец:\n \
                                                                                     подсказка: Кошка - "Мяу"\n \
                                                                                                Собака - "Гав"\n \
                                                                                                Лошадь -  "Иго-го"\n \
                                                                                                Ослик -   "Иа-иа"\n \
                                                                                                Хомяк -   "Фхмфхм" : ')
                    try:
                        if voice in ['Мяу','Гав','Иго-го','Иа-иа','ФхзФхз']:
                            break
                    except Exception:
                        print('Вы привели не знакомое животное, мы не можем поселить его у себя!!!!')
                        continue
                nursery.add_animal(name, age, voice)
                Interface.print_cat()

            elif flag == 4:
                
                print("""                                 СПИСОК ВОЗМОЖНЫХ НАВЫКОВ ДЛЯ ОБУЧЕНИЯ ПО ВИДАМ ПИТОМЦЕВ
                                              Кошки:   'Играть с клубком', 'Ловить мышей', 'Ходить на задних лапах'
                                              Собаки:  'Выполнять команды', 'Бегать за палкой', 'Подавать голос'
                                              Хомяки:  'Бегать в колесе', 'Стучать лапками', 'Грызть палочку'
                                              Лошади:  'Катать упряжку', 'Бегать галопом', 'Прыгать через барьер'
                                              Ослики:  'Катать на себе ребенка', 'Ходить за морковкой', 'Бегать по арене'""")
                Nursery.display_all_animals()
                print('                             Ниже представлены номера занятых вольеров, в которых Вы можете обучить питомцев')
                list_num = create_all_id_animal()
                num_animal = input('                                                \nВведите номер вольера питомца, которого будете обучать: ')
                while int(num_animal) not in list_num:
                    print("                                                     В вольере с указанным номером питомец отсутствует")
                    print("                                                     Заселенные вольеры:")
                    print("                                        ", end = '')
                    for item in list_num:
                        print(item, end='****')
                    print()
                    num_animal = input('                                                Введите номер вольера питомца, которого будете обучать: ')
                skill = input('                                                     Введите навык, которому обучить Вашего питомца:\n')
                Animal.add_skills(int(num_animal), skill)    

            elif flag == 5:
                Nursery.display_all_animals()
                print('                             Ниже представлены номера занятых вольеров, в которых Вы можете просмотреть навыки питомцев')
                list_num = create_all_id_animal()
                num_animal = input('                                                \nВведите номер вольера питомца, навыки которого хотите знать: ')
                while int(num_animal) not in list_num:
                    print("                                                     В вольере с указанным номером питомец отсутствует")
                    print("                                                     Заселенные вольеры:")
                    print("                                        ", end = '')
                    for item in list_num:
                        print(item, end='****')
                    print()
                    num_animal = input('                                                Введите номер вольера питомца, навыки которого хотите знать ')
                skills = Nursery.create_skills_from_number(int(num_animal))
                if skills == '': print(f'                                                        Питомец в вольере {num_animal} ничему не обучен')
                else: print(f"                                                                    Питомец в вольере номер {num_animal} обучен следующим навыкам:\n \
                                                                                {skills}")

        Interface.print_cat()
        print('\t\t\t\t\t\t\t\t\tДо встречи!!! Животным было с Вами очень интересно!!!')

Interface.run()




from db_connector import *

# busy = count_animals()
# print(busy)

def list_to_string(list_skills):
    '''переводит список умений в строку'''
    str_skills = ' '
    if len(list_skills) != 0:
        for skill in list_skills:
            str_skills = str_skills + skill + ','
    return str_skills[:-1]


class Nursery:
    '''Класс Nursery - питомник имеет в атрибутах название питомника name_nursery
    и количество мест (вместимость) number_of_seats'''

    def __init__(self):
        self.name_nursery = "Cheerful farm"
        self.number_of_seats = 30
        self.list_animals = []
    
    def info(self):
        busy_places = count_animals()
        print(f'Питомник: {self.name_nursery},  количество свободных мест:  {self.number_of_seats - busy_places}')

    def add_animal(self, name, age, voice):
        busy_places = count_animals()
        if self.number_of_seats != busy_places:
            new_animal = Animal(name, age, voice)
            add_animal = Nursery.categorize(new_animal)
            #self.list_animals.append(add_animal)
            add_to_db_animal(add_animal.name, add_animal.age, list_to_string(add_animal.learn_skills), add_animal.type)
        else: print('Извините, питомник переполнен!!!')



    @staticmethod
    def categorize(animal):
        
        name, age, voice = animal.name, animal.age, animal.voice
        if animal.voice == "Мяу": 
            animal = Cat(name, age, voice)
            animal.type = 'Кошка'
        elif animal.voice == "Гав": 
            animal = Dog(name, age, voice)
            animal.type = 'Собака'
        elif animal.voice == "ФхзФхз": 
            animal = Humster(name, age, voice)
            animal.type = 'Хомяк'
        elif animal.voice == "Иго-го": 
            animal = Horse(name, age, voice)
            animal.type = 'Лошадь'
        elif animal.voice == "Иа-иа": 
            animal = Donkey(name, age, voice)
            animal.type = 'Ослик'
        else: print('Мы не можем оформить Ваше животное в питомник')
        return animal



class Animal:
    '''класс Animal, который будет родителем для домашних и вьючных'''
    def __init__(self, name, age, voice):
        self.name = name
        self.age = age
        self.voice = voice
        self.type = None
    
    def say(self):
        '''позволяет узнать какой звук издает животное'''
        print(f'Я издаю звук - {self.voice}')
    
    def display_info(self):
        return f'Кличка: {self.name}, возраст: {self.age}'
    

    def add_skills(self, skill):
        '''позволяет добавить навык питомцу, если он имеется в списке базовых для него'''
        print(f'Список возможных для обучения навыков: \n {self.skills}')
        if skill not in self.skills: print ('В нашем приемнике этому не учат!!!')
        elif skill in self.learn_skills: print ('Ваш питомец уже обучен этому навыку!')
        else:
            self.learn_skills.append(skill)
            print(f"Ваш питомец успешно освоил навык {skill}")

    def display_skills(self):
        '''демонстрирует каким навыкам уже обучен питомец'''
        self.display_info()
        print('Ваш питомец обучен следующим навыкам:')
        for skill in self.learn_skills:
            print(skill)



        

class Pets(Animal):
    def __init__(self, name, age, voice):
        super().__init__(name, age, voice)
        self.place_of_life = "Проживает дома с человеком"

class Packs(Animal):
    def __init__(self, name, age, voice):
        super().__init__(name, age, voice)
        self.place_of_life = "Проживает в загоне (дворе)"

class Cat(Pets, Animal):
    
    def __init__(self, name, age, voice):
        super().__init__(name, age, voice)
        self.skills = ['Играть с клубком', 'Ловить мышей', 'Ходить на задних лапах']
        self.learn_skills = []
    
    def display_info(self):
        print (super().display_info() + ' ' + f'{self.type}')

class Dog(Pets, Animal):
    
    def __init__(self, name, age, voice):
        super().__init__(name, age, voice)
        self.skills = ['Выполнять команды', 'Бегать за палкой', 'Подавать голос']
        self.learn_skills = []
    
    def display_info(self):
        print (super().display_info() + ' ' + f'{self.type}')

class Humster(Pets, Animal):
    
    def __init__(self, name, age, voice):
        super().__init__(name, age, voice)
        self.skills = ['Бегать в колесе', 'Стучать лапками', 'Грызть палочку']
        self.learn_skills = []  
    
    def display_info(self):
        print (super().display_info() + ' ' + f'{self.type}')
    
class Horse(Packs, Animal):
    
    def __init__(self, name, age, voice):
        super().__init__(name, age, voice)
        self.skills = ['Катать упряжку', 'Бегать галопом', 'Прыгать через барьер']
        self.learn_skills = []  
    
    def display_info(self):
        print (super().display_info() + ' ' + f'{self.type}')
    
class Donkey(Packs, Animal):
    
    def __init__(self, name, age, voice):
        super().__init__(name, age, voice)
        self.skills = ['Катать на себе ребенка', 'Ходить за морковкой', 'Бегать по арене']
        self.learn_skills = []

    def display_info(self):
        print (super().display_info() + ' ' + f'{self.type}')  

nursery_val = Nursery()
nursery_val.info()

#add_animal = Nursery.categorize(Animal("Понька", 12, "Иа-иа"))
#print(list_to_string(add_animal.learn_skills))
#nursery_val.add_animal("Леопольд", 8, "Мяу")

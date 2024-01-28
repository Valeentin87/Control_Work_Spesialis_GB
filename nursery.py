class Nursery:
    '''Класс Nursery - питомник имеет в атрибутах название питомника name_nursery
    и количество свободных мест number_of_seats'''

    def __init__(self):
        self.name_nursery = "Cheerful farm"
        self.number_of_seats = 30
    
    def info(self):
        print(f'Питомник: {self.name_nursery},  количество свободных мест:  {self.number_of_seats}')



class Animal:
    '''класс Animal, который будет родителем для домашних и вьючных'''
    def __init__(self, name, age, voice):
        self.name = name
        self.age = age
        self.voice = voice
    
    def say(self):
        '''позволяет узнать какой звук издает животное'''
        print(f'Я издаю звук - {self.voice}')

class Pets(Animal):
    def __init__(self, name, age, voice):
        super().__init__(name, age, voice)
        self.place_of_life = "Проживает дома с человеком"
    
    
    
    




nursery_valentin = Nursery();
nursery_valentin.info()

barsik = Pets('Барсик', 12, 'Мяу')
barsik.say()
print(barsik.place_of_life)

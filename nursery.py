class Nursery:
    '''Класс Nursery - питомник имеет в атрибутах название питомника name_nursery
    и количество свободных мест number_of_seats'''

    def __init__(self):
        self.name_nursery = "Cheerful farm"
        self.number_of_seats = 30
    
    def info(self):
        print(f'Питомник: {self.name_nursery},  количество свободных мест:  {self.number_of_seats}')



nursery_valentin = Nursery();
nursery_valentin.info()
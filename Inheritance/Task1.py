"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def print_info(self):
        print('Имя:', name, '\nСостояние здоровья:', health)


class Magician(Hero):
    def hello(self):
        print('Новый герой! На поле появляется Маг по имени', name)
        self.print_info
    
    def atack(self):
        print('Удар! Маг', self.name, 'атакует врага магией.')
    
#меня не было, я не поняла, что именно мне тут писать, но было весело, хехе

"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""


class Duck():
    def sound(self):
        return "Кряя!"

    def dress(self):
        return "Ты придурок? Я не могу носить одежду :/"


class Human():
    def sound(self):
        return "*Имитация кряканья. Выглядит жалко.*"

    def dress(self):
        return "Ура! Я ношу одежду."


human = Human()
duc4 = Duck()

for animal in (human, duc4):
    print(animal.sound())
    print(animal.dress())
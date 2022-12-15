"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""


class SpaceObject:
    def __init__(self, size):
        self.size = size


class Star(SpaceObject):
    def __init__(self, size, brightness):
        super().__init__(size)
        self.brightness = brightness

    def shine(self):
        print(f"Светит с яркостью {self.brightness}")


class Planet(SpaceObject):
    def __init__(self, population, add):
        self.population = population
        self.add = add

    def add_after(self, ears):
        self.population += self.add * ears
        print(f"Спустя {ears} лет население на планете будет {self.population} человек.")


Moon = Star(200, "7 из 10")
Moon.shine()

Earth = Planet(22, 5)
Earth.add_after(5)
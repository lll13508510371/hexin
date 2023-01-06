"""
请用面向对象的继承的方式实现以下类的封装:

    动物类（Animal）：
        属性：name, high, weight
        行为：吃

    老虎类（Tiger）：
        属性：name, high, weight
        行为：吃、老虎的狩猎技能

    狮子类（Lion）：
        属性：name, high, weight
        行为：吃、狮子的狩猎技能

    狮虎兽（Liger）：
        属性：name, high, weight
        行为：吃、既有老虎的狩猎技能、也有狮子的狩猎技能
"""


class Animal:
    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        print(f'{self.name}能吃')


class Tiger(Animal):
    def __init__(self, name, high, weight):
        super().__init__(name, high, weight)

    def eat(self):
        super().eat()

    def hunt(self):
        print(f'{self.name}有老虎的狩猎技能')


class Lion(Animal):
    def __init__(self, name, high, weight):
        super().__init__(name, high, weight)

    def eat(self):
        super().eat()

    def hunt(self):
        print(f'{self.name}有狮子的狩猎技能')


class Liger(Lion, Tiger, Animal):
    def __init__(self, name, high, weight):
        super().__init__(name, high, weight)

    def eat(self):
        super().eat()

    def hunt(self):
        super().hunt()
        Tiger.hunt(self)


Liger1 = Liger('狮虎兽1', 50, 290)
Liger1.eat()
Liger1.hunt()

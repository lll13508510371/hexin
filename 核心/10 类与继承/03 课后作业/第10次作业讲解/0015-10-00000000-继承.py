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
        return f'{self.name} 正在吃东西'

class Tiger(Animal):
    # 重写 吃东西的行为
    def eat(self):
        return f'{self.name} 正在吃东西, 释放了[老虎]的狩猎技能'

class Lion(Animal):
    # 重写 吃东西的行为
    def eat(self):
        return f'{self.name} 正在吃东西, 释放了[狮子]的狩猎技能'

class Liger(Tiger, Lion):
    # 重写 吃东西的行为
    # def eat(self):
    #     return f'{self.name} 正在吃东西, 释放了[狮子]的狩猎技能'
    def eat(self):
        return f'{self.name} 正在吃东西'

    def tiger_eat(self):
        """定义一个调用老虎类吃东西的方法"""
        Tiger.__init__(self, self.name, self.high, self.weight)
        return Tiger.eat(self)

    def lion_eat(self):
        """定义一个调用狮子类吃东西的方法"""
        Lion.__init__(self, self.name, self.high, self.weight)
        return Lion.eat(self)

liger = Liger('狮虎兽', '250cm', '480kg')
print(liger.eat())
print(liger.tiger_eat())
print(liger.lion_eat())


# 将列表中字典的学生对象, 转化成了 Student的类的实例对象
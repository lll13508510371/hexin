class Animal:
    """动物类"""

    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        return self.name + ' 正在吃东西'


# 犬科类
class Dog(Animal):
    def __init__(self, name, high, weight, color):
        super().__init__(name, high, weight)
        self.color = color

    # 定义了一个父类中没有的方法, 可以直接通过子类对象调用, 父类对象不能调用
    # 动物叫的方法
    def bark(self):
        return f'{self.name} 正在嗷呜叫~~~~'

    # 重写父类对象的方法, 先把父类的方法拿过来
    def eat(self):
        # super().eat()  调用父类的方法, 然后拓展
        return super().eat() + '  发出咔咔咔的声音'


dog1 = Dog('tom', '50cm', '30kg', '黑色')
print(dog1.color)
print(dog1.bark())
print(dog1.eat())

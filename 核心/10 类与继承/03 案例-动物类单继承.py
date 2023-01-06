class Animal:
    """动物类"""

    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        return self.name + ' 正在吃东西'


class Dog(Animal):
    def __init__(self, name, high, weight):
        # 子承父业, 子可以在父的基础上创新, 添加...
        super().__init__(name, high, weight)


dog1 = Dog('哈士奇', '50cm', '30kg')
print(dog1.name)
print(dog1.high)
print(dog1.weight)
print(dog1.eat())

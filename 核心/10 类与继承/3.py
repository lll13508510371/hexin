class Animal:
    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight


class Dog(Animal):
    def __init__(self, name, high, weight):
        super().__init__(name, high, weight)


dog1 = Dog('哈士奇', '50cm', '30kg')  # 实例对象dog1 类对象Dog
print(dog1.name)

'''
绑定到子类的self之后 --> self.
'''
class Animal:
    """动物类"""
    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        return self.name + ' 正在吃东西'

# 犬科类
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color


# 狼类
class Woolf(Dog, Animal):
    pass


# woolf = Woolf('狼大', '50cm', '30kg')
# print(woolf.name)
# print(woolf.high)
# print(woolf.weight)
# print(woolf.eat())

woolf = Woolf('狼大', '灰色')
print(woolf.name)
# print(woolf.high)
# print(woolf.weight)
print(woolf.color)
print(woolf.eat())

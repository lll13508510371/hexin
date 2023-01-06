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
    # 基于继承父类属性的基础上, 新增子类属性
    # 首先要重写方法
    def __init__(self, name, high, weight, color):  # color 是基于继承关系新增的属性
        super().__init__(name, high, weight)  # 继承父类的属性, 需要把父类的属性绑定到子类中继承
        self.color = color  # 把新增的属性绑定到子类对象上


tiger1 = Animal('老虎', '150cm', '100kg')
print(tiger1.name)
print(tiger1.high)
print(tiger1.weight)

dog1 = Dog('tom', '50cm', '30kg', '黑色')
print(dog1.color)

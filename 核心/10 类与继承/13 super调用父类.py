class PracticeBody:
    """炼体期"""
    class_attribute = 1

    def __init__(self, name, blood, power):
        self.blood = blood
        self.power = power

    def carry_water(self):
        self.power -= 2

    def chop_wood(self):
        self.power -= 3


class PracticeMagic(PracticeBody):
    """练气"""

    def __init__(self, name, blood, power, magical_power):
        # 继承父类的属性
        super().__init__(name, blood, power)
        self.magical_power = magical_power

    def carry_water(self):
        # 写法1: super(父类名-->应该是子类名吧?, self).方法()  无法调用属性
        # print(super(PracticeMagic, self).blood)
        # print(self.blood)
        # super()指的是父类,里面默认绑定了self, e.g. super(PracticeMagic, self) --> python 2.0 -->python 3.0 就直接用super()
        # super()
        # 写法2: super().父类方法(), 无法调用属性

        super().carry_water()
        '''
        !!!!!!super()指父类对象,类对象可以调用方法和类属性,但无法调用实例对象属性,下面我调用了一个类属性,得到了结果!!!
        '''
        print(super().class_attribute)

    def chop_wood(self):
        self.magical_power -= 0.3

    def fly(self):
        self.magical_power -= 2

    def spurt_fire(self):
        self.magical_power -= 2


zs = PracticeMagic('张三', 1000, 100, 100)
zs.carry_water()
print(zs.power)

print(super(PracticeMagic, zs))

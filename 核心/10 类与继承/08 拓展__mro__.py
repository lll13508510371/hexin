# 师傅类
class Master(object):
    def __init__(self):
        self.secret = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.secret}制作煎饼果子')


# 学校类
class School(object):
    def __init__(self):
        self.secret = '[青灯煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.secret}制作煎饼果子')


# 徒弟类, 继承自师傅类
class Prentice(School, Master):
    def __init__(self):  # 重写方法需要和父类的名字一样
        super().__init__()
        self.secret = '[独创煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.secret}制作煎饼果子')

    def make_master_cake(self):
        Master.make_cake(self)  # 类对象调用

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


print(Prentice.__mro__)
"""
    查找顺序:
        先找本身有没有属性或者方法 --> 父类对象 (优先级)  --> 在基类中查找  --> 报错
"""

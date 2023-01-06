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


# 结论: 如果子类中和父类有同名的属性和方法
#       那么在子类对象调用属性或者方法的时候, 会调用自己的
wanzi = Prentice()
wanzi.make_cake()

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
        Master.__init__(self)
        Master.make_cake(self)  # 类对象调用

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 徒孙类
class Tusun(Prentice):
    pass


# 不推荐大家用中文变量命名
自游 = Tusun()
自游.make_cake()
自游.make_master_cake()  # 调用师傅类封装的方法
自游.make_school_cake()  # 调用学校类封装的方法

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

    # 调用师傅类的方法: 把父类中同名的属性和方法封装
    def make_master_cake(self):
        # !!!!父类名.__init__(), 调用父类的初始化属性, 需要绑定到子类对象来--> 需要添加self
        Master.__init__(self)
        Master.make_cake(self)  # 类对象调用

    def make_school_cake(self):
        # 父类名.__init__(), 调用父类的初始化属性, 需要绑定到子类对象来--> 需要添加self
        School.__init__(self)
        School.make_cake(self)


wanzi = Prentice()
wanzi.make_cake()
wanzi.make_master_cake()  # 调用师傅类封装的方法
wanzi.make_school_cake()  # 调用学校类封装的方法

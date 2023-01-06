# 师傅类
class Master(object):
    # def __init__(self):
    #     self.secret = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用[古法煎饼果子配方]制作煎饼果子')


# 学校类
class School(object):
    # def __init__(self):
    #     self.secret_1 = '[青灯煎饼果子配方]'

    def make_cake_1(self):
        print(f'运用[青灯煎饼果子配方]制作煎饼果子')


# 徒弟类, 继承自师傅类
class Prentice(School, Master):
    # 多继承, 同时继承 Master(师傅类) 和 School(学校)
    # 如果继承的类具有相同的属性或者方法, 那么会调用离子类名字最近的类的属性或者方法 (谁在前面谁是爹)

    # 在多继承关系中, 会有优先继承关系, 满足就近原则, 否则报错

    # 如果在多继承关系中没有定义属性, 那么父类的所有方法都可以调用
    pass


# 继承关系中可以调用父类的所有属性和方法
wanzi = Prentice()
# print(wanzi.secret)
wanzi.make_cake()
wanzi.make_cake_1()

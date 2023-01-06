# 师傅类
class Master(object):
    def __init__(self):
        self.secret = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.secret}制作煎饼果子')


# 徒弟类, 继承自师傅类
class Prentice(Master):
    pass


# 继承关系中可以调用父类的所有属性和方法
wanzi = Prentice()
print(wanzi.secret)
print(wanzi.make_cake())

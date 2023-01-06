# object 代表基类, 任何的Python类都会默认继承自基类
# 如果单单只继承基类, 那么可以省略
class A(object):  # --> 在类中类名后的圆括号是用来显示继承关系的, 不是参数
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


class B(A):  # B 类继承 A类
    pass  # pass 代码站位


result = B()
print(result.num)  # 因为 B 类继承 A类, 会继承父类的属性
result.info_print()  # 因为 B 类继承 A类, 会继承父类的方法
print(B)

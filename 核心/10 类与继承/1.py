# object 代表基类, 任何的Python类都会默认继承自基类 --> 任何Python类的祖宗
# 如果只是继承基类,就可以省略
class A(object):  # --> 在类中 类名后的括号是用来显示继承关系的,不是参数
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


class B(A):  # B 类继承 A类
    pass  # pass 代码占位--> 不知道写什么,用pass不会报错


'''# pass 代码占位--> 不知道写什么,用pass不会报错'''

result = B()  # 实例化对象
print(result)
print(result.num)
result.info_print()

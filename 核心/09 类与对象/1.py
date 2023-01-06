# print(10000 / 24)

'''
类:群体
对象:个体
'''


class Student:
    # 类有属性: 实例属性, 类属性
    # 类有方法: 行为
    # 用函数来封装

    # 初始化函数, 只有在类当中会有特殊的作用
    # 作用:在后续实例化创建对象的时候,会默认被调用
    # 初始化函数在调用的时候,如果有参数,这个参数就叫做实例属性 --> 实例化的对象的属性
    def __init__(self, name, score, sex):
        '''

        :param name: 实例属性
        :param score: 实例属性

        '''
        self.name = name
        self.score = score
        self.sex = sex

    # 对象的方法
    # 可以在方法中引用实例属性
    # 方法得通过对象调用
    def print_info(self):
        print(f'姓名:{self.name}, 分数:{self.score}, 性别:{self.sex}')


'''
实例化对象
'''

# 类名+()根据类创建对象,可以根据类创建多个相同属性的对象
# 有实例属性就在()中传参数,不传就会报错
person1 = Student('路景涵', 100, '男')
# 打印person1是一个对象
print(person1)
# 对象有对象的方法.这里person1对象可以调用它的方法
person1.print_info()

# !模具 --> 生产很多类似的产品

person2 = Student('丸子', 99, "女")
person2.print_info()
print(person1.name)

''' !!!!!!!!!!!!!!!!!!!!!!!!!!!
# 列表,元组,字典,集合
# !!!列表 ---> 根据索引取值 是列表的属性
'''

'''
全栈会用到类方法
(用的少不代表不用) --> (盐吃的少不代表不吃盐)
'''

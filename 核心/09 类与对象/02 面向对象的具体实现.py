"""面向过程创建对象"""
stu1 = {'name': '小明', 'score': 90}
stu2 = {'name': '正心', 'score': 90}

def print_info(student):
    print(f'姓名: {student["name"]}, 分数: {student["score"]}')

# print_info(stu1)
# print_info(stu2)

# class 申明一个类的关键字, 我要创建一个类了
# 类名首字母一般大写 --> 大驼峰命名法
class Student:
    # 类有属性: 实例属性, 类属性
    # 类有方法: 行为  实例方法, 类方法

    # 初始化函数, 只有在类当中会有特殊的作用
    # 作用: 在后续实例化创建对象的时候, 会默认的被调用
    # 初始化函数在调用的时候, 如果有参数, 这个参数就叫做实例属性 --> 实例化的对象的属性
    def __init__(self, name, score, sex):
        self.name = name  # 姓名属性
        self.score = score  # 分数属性
        self.sex = sex  # 性别属性

    # 对象的方法
    # 可以在方法中引用实例属性
    # 方法得通过对象调用
    def print_info(self):
        print(f'姓名: {self.name}, 分数: {self.score}')

    def eat(self):
        print(f'{self.name} 在吃东西')

"""实例化对象操作"""
# 类名+()  根据类创建对象, 可以根据类创建多个相同属性的对象
# 有实例属性就在 () 中传递实例属性, 不传就报错
person1 = Student('正心', 100, '男')
print(person1)

# 实例化对象后, 可以调用对象的方法
person1.print_info()
person1.eat()


# 模具 --> 生产很多类似的产品

person2 = Student('丸子', 99, '女')
person2.print_info()
person2.eat()

# 对象有对象的属性, 对象有对象的方法
print(person1.name)
print(person2.sex)

# 列表 元组 字典 集合 ---> 对象
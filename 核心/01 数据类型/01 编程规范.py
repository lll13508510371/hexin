"""注释"""

# 一个 # 号代表单行注释, 可以针对某一行代码进行注释说明

str1 = "123"

"""
多
行
注
释
"""

'''
多
行
注
释
'''

# ctrl + /  注释的快捷键

# 注释的作用: 仅针对代码说明, 解释器在遇到注释的时候会自动跳过
# 注释是给人看的 ---> 程序员

"""标识符(变量)命名"""
# 1. 组成: 字母, 数字, 下划线
# 2. 不能以数字开头

name = '山禾'
my_name = '自游'
my_name123 = '巳月'

# 12my_name = '正心'


_123 = '思语'

_ = '恺恺'

print(name)
print(my_name)
print(my_name123)
# print(12my_name)
print(_123)
print(_)

"""团队规范"""
hello_world = 'hello_world'  # 满足国人习惯
HelloWorld = 'hello_world'  # 外国人的习惯
jelloWorld = 'hello_world'

# Ctrl + Alt + L<字母>   快速格式化代码的快捷键, 帮助我们尽量的满足pep8的代码规范

# print(name)
"""
    NameError: name 'name' is not defined
    名称错误：name 没有被定义
"""

# print(10 / 0)
"""
    ZeroDivisionError: division by zero
    除零错误：任何数值被零除都会导致ZeroDivisionError错误
"""

# for
"""
    SyntaxError: invalid syntax
    语法错误：python语法有问题
"""

list_a = [1, 2, 3, 4, 5]
# print(list_a[10])
"""
    IndexError: list index out of range
    索引错误：使用一个超出范围的值索引时引发
"""

data_dict = {'name': '正心'}
# print(data_dict['age'])
"""
    KeyError: 'age'
    键错误：改字典没有这个键引发的报错
"""

list_b = [1, 2, 3, 4, 5]
# list_b.split()
"""
    AttributeError: 'list' object has no attribute 'split'
    属性错误：对象没有该属性或方法引发的报错
"""
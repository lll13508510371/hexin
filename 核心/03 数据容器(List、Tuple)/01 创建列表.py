
'''
在变量命名的时候不要用关键字和常见函数名对变量命名 str int float True False  input print  type
[] (中括号) 列表
# <class 'list'>  list --> 指代列表数据类型
# 列表是一个数据容器, 我们可以在里面放置数据, 任意的数据类型都可以放置
'''
list1 = [1, 2, 3, 'a', 'b', 'c', True, False, 3 > 4, print(),print]

print(list1)
print(type(list1))

"""不同类型的数据转化"""
print(str([1, 2, 3, 'a', 'b', 'c', True, False, 3 > 4, print]))
print(type(str([1, 2, 3, 'a', 'b', 'c', True, False, 3 > 4, print])))

# 有序列的数据类型可以直接互相转化

"""数据容器: 增删改查"""

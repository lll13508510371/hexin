# 元组是一种不可变的,有序的数据容器

# <class 'tuple'>  --> 元组
tup1 = (1, 2, 3, 4)
# 查看元组的数据类型
print(tup1)
print(type(tup1))

print(tup1[2])
print(tup1[2:])

# 元组不可修改
# tup1[2] = 10 类与继承

# 元组只支持数据查找, 查找的方法和列表一致
print(tup1.index(1))
print(tup1.count(1))
print(len(tup1))


# 创建一个只有一个数据的元组, 要在这个数据后面加逗号
tup2 = ('63')
print(tup2)
print(type(tup2))

tup3 = ('63',)
print(tup3)
print(type(tup3))
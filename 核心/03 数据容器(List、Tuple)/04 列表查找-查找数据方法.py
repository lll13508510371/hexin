list1 = [4, 2, 1, 0, 6, 2]
# index() 方法, 方法中传入一个元素,就会得到元素在列表中第一次出现的下标/索引
# 如果元素不存在就会报错
print(list1.index(2))
# print(list1.index(9))

"""列表中有重复的数据，要统计某个重复的数据出现的次数"""
print(list1.count(2))  # 2 这个元素在列表中出现了2次
print(list1.count(4))  # 2 这个元素在列表中出现了2次

"""想知道列表中数据量有多少？"""
print(len(list1))  # list1 这个列表中有6个数据 <是数据个数， 不是索引>

# in 判断某个数据在不在列表里面
print(10 in list1)
print(6 in list1)

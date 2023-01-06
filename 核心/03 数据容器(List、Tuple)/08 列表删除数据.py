list1 = ['a', 'b', 'c', 'd', 'e', 'f']

# pop()     默认删除最后一个元素
# list1.pop()
# list1.pop()
# list1.pop(1)  # 删除索引为 1 的数据
# pop() 可以指定位置进行删除, 根据下标删除数据(会修改原有的列表)

result = list1.pop(3)  # pop可以用变量接受, 得到删除的内容

print(result)

list1.remove('b')  # 注意是指定元素, 不是指定列表的下标

print(list1)

result1 = list1.remove('b')

print(result1)

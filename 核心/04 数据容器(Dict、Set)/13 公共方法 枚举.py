"""enumerate()"""

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
list1 = ['a', 'b', 'c', 'd', 'e']
#
# print(list(enumerate(list1)))

for index, data in enumerate(list1):
    print(f'索引是: {index}, 值是: {data}')

# 枚举法

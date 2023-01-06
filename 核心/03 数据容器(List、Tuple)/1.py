'''
有序列的数据类型之间可以转换
'''
# list1 = [1,2,22222,2,22]
# print(list1.index(2))
# print(list1.count(2))
# print(len(list1))
# print(3 in list1)

'''
导入random内置模块
'''
import random
# 格式化输出
import pprint

# name_list = ['正心', '丸子', '自游']
# name_list2 = ['巳月', '落落', '自游']
# name_list3 = [3, 2, 1, 5, 7, 4]
# name = input('请输出要查找的名字:')
#
# if name in name_list:
#     print(f'{name},"存在"')
# else:
#     print(f'{name},"不存在"')
'''
列表能接受所有类型的数据
'''
# name_list.append('思语')
# print(name_list)
# name_list.append(name_list2)
# print(name_list)
# name_list.extend(name_list2)
# print(name_list)
# print(name_list + name_list2)
# name_list.insert(2, ['巳月'])
# print(name_list)
# for index in range(len(name_list2)):
#     if name_list2[index] not in name_list:
#         name_list.append(name_list2[index])
#         print(name_list)
#     else:
#         print('重复的数据', name_list2[index])
#         print('重复的索引', index)
#         print('重复个数', name_list.index(name_list2[index]))

# name_list.pop(2)
# print(name_list)
# result = name_list.pop(2)
# print(result)

# name_list.remove('自游')
# print(name_list)
# print(name_list.remove('自游'))

# name_list[2] = '思雨'
# print(name_list)

# name_list.reverse()
# print(name_list)

'''
!!!
# name_list3.sort()
# print(name_list3)
# name_list3.sort(reverse=True)
# print(name_list3)
'''

# i = 0
# while i < len(name_list):
#     print(name_list[i])
#     i += 1

'''
!!!
# 直接遍历循环列表
for i in name_list:
    print(i)
# 根据列表索引取值
for i in range(len(name_list)):
    print(name_list[i])
'''
# print(random.randint(1,3))
# list1 = []
#
# for i in range(10 类与继承):
#     list1.append(random.randint(1,10 类与继承))
#
# print(list1)
'''
list2 = [name_list] + [name_list2]
print(list2)
print(list2[1][1])
'''
# tup = ((63))
# print(type(tup))
# tup = (63,)
# print(type(tup))

name = '小明,小红,小六,老八,巴适,六,了,开票,落落'
list1 = ['第一名', '第二名', '第三名', '第四名', '第四名','第四名','第四名','第四名','第四名']
name_list = name.split(',')
print(name_list)

list2 = []
for index in range(len(list1)):
    list2.append([name_list[index],list1[index]])

print(list2)
print(type(list2))
pprint.pprint(list2)


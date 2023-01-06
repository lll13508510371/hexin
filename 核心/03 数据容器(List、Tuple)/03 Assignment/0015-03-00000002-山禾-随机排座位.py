# -*- coding: utf-8 -*-
"""
作业1：
有N个人要参加会议，现在需要随机安排座位。
请用python实现将N个人随机安排座位

提示：
    可以导入随机函数模块 random
    random.randint(a, b)
    Return random integer in range [a, b], including both end points.
    在 [a, b] 之间返回一个随机整数，包括 a, b 本身。
"""
import pprint
import random

name = """
邓永明    廖德超    张勇 杨久林    戴贵富    秦代坤    李元东 田显余
"""
# 有多少个人
name_list = name.split()

site_list = ['1号办公室1位置', '1号办公室2位置', '1号办公室3位置',
             '2号办公室1位置', '2号办公室2位置', '2号办公室3位置',
             '3号办公室1位置', '3号办公室2位置']

# 答案放这里
seating = []
# 答案以二维列表输出 [('1号办公室1位置', '秦代坤'), ('1号办公室2位置', '廖德超'),.......]
"""自己在下方编写代码实现功能"""
# print(name_list)
'''
 随机生成0 - 7并且不重复
'''
'''
# Method1
number = random.sample(range(0, 8), 8)
# print(number)
i = 0
for num in number:
    seating.append((site_list[i], name_list[num]))
    i += 1
    # print(seating)
print(seating)
pprint.pprint(seating)
'''

'''
# Method 2 随机座位或者随机人
'''
"""for i in range(len(name_list)):
    person = name_list.pop(random.randint(0, len(name_list) - 1))
    seating.append((site_list[i], person))
print(seating)
pprint.pprint(seating)
print(random.randint(0, 0))"""


"""for i in range(len(site_list)):
    seat = site_list.pop(random.randint(0, len(site_list) - 1))
    seating.append((seat, name_list[i]))
print(seating)
pprint.pprint(seating)"""


'''
# Method 3 随机座位随机人
'''
for i in range(len(name_list)):
    person = name_list.pop(random.randint(0, len(name_list) - 1))
    print(person)
    seat = site_list.pop(random.randint(0, len(site_list) - 1))
    print(seat)
    seating.append((seat, person))
    print(seating)

print(seating)
pprint.pprint(seating)
print(random.randint(0, 0))
'''
pop一个列表元素之后,列表索引随之减少一个

如果要写多种方法,写完一个要注释掉前面方法的代码
'''

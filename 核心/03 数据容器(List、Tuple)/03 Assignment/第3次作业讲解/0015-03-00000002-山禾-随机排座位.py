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
import pprint

# 随机安排座位: 人<人随机>   座位<随机>

# 人随机
# for i in range(len(name_list)):  # 构建索引的循环 01234567
#
#     index = random.randint(0, len(name_list) - 1)
#     data = name_list.pop(index)
#     print(name_list)
#     seating.append([data, site_list[i]])
#
# pprint.pprint(seating)

# 座位随机
for i in range(len(site_list)):  # 构建索引的循环 01234567

    index = random.randint(0, len(site_list) - 1)
    data = site_list.pop(index)
    print(name_list)
    seating.append([data, name_list[i]])

pprint.pprint(seating)

# -*- coding: utf-8 -*-
import copy

# c = []
# a = [1, 2, 3]
# c.append(copy.copy(a))  # 第一次添加 a
# print(c)
# a.append(4)
# c.append(copy.copy(a))  # 第二次添加 a
# print(c)
# a.append(5)
# c.append(copy.copy(a))  # 第三次添加 a
# print(c)
with open('../../../核心/07 文件与深浅拷贝/01 上课代码/text2.txt', mode='w') as f:
    f.write('1\n')
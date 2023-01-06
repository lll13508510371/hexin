# -*- coding: utf-8 -*-
# encoding = utf-8
import copy  # 深浅拷贝的模块, 内置模块

array2 = [1,
          ['a', 'b', 'c'],
          3]

# # 深拷贝, 把对象里面的内容全部赋值一份(所有维度的数据)
arr2 = copy.deepcopy(array2)

array2[1][0] = 100

print(array2)
print(arr2)

# 浅拷贝的作用域仅限在一维的维度

# -*- coding: utf-8 -*-
"""
定义一个函数，对传入未知个长度的内容进行求和并且返回

传入的内容如下(print里面的东西)

"""

# print(1,2,3,4,5,a=6,b=7,c=8)

"""自己在下方编写代码实现功能"""


# 不定长参数的使用  *args  **kwargs

def get_sum(*args, **kwargs):
    print(args)
    print(kwargs)

    total = 0
    for i in args:
        total += i

    for j in kwargs.values():
        total += j

    return total


print(get_sum(1, 2, 3, 4, 5, a=6, b=7, c=8))

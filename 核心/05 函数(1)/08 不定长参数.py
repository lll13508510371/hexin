"""
假设一个班有N个学员
假设 N 为 3 ，体重分别是 180、190、200
请编写一个函数对整个班级的学员的体重求和
"""


def get_weight(stu1, stu2, stu3):
    total = stu1 + stu2 + stu3
    return total


stu1 = 180
stu2 = 190
stu3 = 200


# print(get_weight(stu1, stu2, stu3))

# *args  接受所有传进来的位置参数
def sum_weight(*args):
    print(args)
    print(type(args))

    total = 0
    for i in args:
        total += i
    return total


# print(sum_weight(1, 2, 3, 4, 5, 6))
# print(sum_weight(1, 2, 3, 4, 5, 6, 7, 8))

# **kwargs 用于接受所有传进来的关键字参数
def sum_weight_2(**kwargs):
    print(kwargs)
    print(type(kwargs))


sum_weight_2(a='a', b='b', c='c')
sum_weight_2(a=1, b=2, c=3)

"""
假设一个班有N个学员
假设 N 为 3 ，体重分别是 180、190、200
请编写一个函数对整个班级的学员的体重求和
"""


def get_weight(*args, **kwargs):
    """

    :param args: 接受的所有的位置参数
    :param kwargs: 接受所有的关键字参数
    :return:
    """
    print(args)
    print(kwargs)


get_weight(60, 70, 80, 65, 同学1=63, 同学2=64, 同学3=65)

def fuc1(stu1, stu2, stu3):
    total = stu1 + stu2 + stu3
    return total


stu1 = 159
stu2 = 133
stu3 = 134


def sum_weight(*args):
    print(args)
    print(type(args))
    total = 0
    for i in args:
        total += 1
    return total


print(sum_weight(1, 2, 3, 4, 5, 6, 7))


def sum_weight_2(**kwargs):
    '''

    :param kwargs: 关键词参数
    :return: 关键词
    '''

    print(kwargs)
    print(type(kwargs))


sum_weight_2(a='a', b='j', c=1)



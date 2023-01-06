list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    return x % 2 == 0  # 过滤序列中数据所有的基数


# result = filter(func, list1)
result = filter(lambda x: x % 2 == 0, list1)
print(result)
print(list(result))

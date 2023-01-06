import functools
'''
reduce --> 缩小
'''
c = [6, 7, 8, 9]


def func(a, b):
    return a + b


# 累计运算的方法 func() --> 调用函数, 得到函数返回结果
result = functools.reduce(func, c)
# result = functools.reduce(lambda x, y: x + y, c)
print(result)

print(lambda x, y: x)
print(func)
list1 = [1, 2, 3, 4, 5]


def func(x):
    return x ** 2


# result = map(func, list1) map --> 变换;改变 --> 这里直接把列表改了
result = map(lambda x: x ** 2, list1)
print(result)
print(list(result))

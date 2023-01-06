"""
把列表中所有人都变成sb,比方: Tencent_sb
"""
name = ['Tencent', 'Zhihu', 'Baidu']

"""请在下方编辑代码"""
# 学习内容 --> 函数

def func(x):  # --> 一定需要设置参数
    print(x)
    return x + '_sb'  # return返回的结果就是最终的替换结果


result = map(func, name)   # name 列表中每一个数据都会传入到指定的函数(func),
                            # 参数指代的就是列表每一个数据
print(list(result))


# 匿名函数
result2 = map(lambda x: x + '_sb', name)
print(list(result2))

# 列表推导式
print([i + '_sb' for i in name])